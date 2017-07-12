import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
from time import sleep

import global_variables
import data_builder
from UI import collectwidget


def resize_image(src, width, height):
    src_height, src_width = src.shape[:2]
    factor_width = width / src_width
    factor_height = height / src_height
    if src_height * factor_width > height:
        factor = factor_height
    else:
        factor = factor_width
    return cv2.resize(src, (int(factor * src_width), int(factor * src_height)), interpolation=cv2.INTER_CUBIC)


def read_file_to_string_array(file_path):
    result = []
    with open(file_path) as f:
        for line in f:
            result.append(line)
    return result


class JHCaptureThread(QtCore.QThread):

    def __init__(self, gui_parent):
        QtCore.QThread.__init__(self)
        self.gui_parent = gui_parent

    def run(self):
        requirements = read_file_to_string_array(global_variables.COLLECTOR_REQUIREMENTS_PATH)
        try:
            step_num_of_images = int(int(requirements[0]) / (len(requirements) - 1))
        except ValueError or IndexError:
            msg = QtWidgets.QMessageBox()
            msg.setText("No requirement detected")
            msg.setWindowTitle("Message")
            retval = msg.exec_()
            self.gui_parent.startButton.setDisabled(False)
            return

        requirements.remove(requirements[0])
        for requirement in requirements:
            self.gui_parent.statusLabel.setText(requirement)
            sleep(4)
            num_of_captured = 0
            while num_of_captured < step_num_of_images:
                added = self.gui_parent.add_data(self.gui_parent.name)
                num_of_captured += added

        self.gui_parent.statusLabel.setText("Tất cả đã xong, xin cảm ơn")
        sleep(4)
        self.gui_parent.statusLabel.setText("﻿Click \"start\" to begin")

        self.gui_parent.startButton.setDisabled(False)


class JHDataCollectorGUI(QtWidgets.QWidget, collectwidget.Ui_mainForm):
    def __init__(self, parent=None):
        super(JHDataCollectorGUI, self).__init__(parent)

        self.data_builder = data_builder.DataBuilder(global_variables.DATA_PATH)
        self.face_cascade = cv2.CascadeClassifier(global_variables.CASCADE_PATH)
        self.num_of_faces = 0

        self.setupUi(self)

        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.cameraLabel.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cameraLabel.height())

        _, self.current_image = self.capture.read()
        self.capture_thread = JHCaptureThread(self)
        self.name = ''
        self.startButton.clicked.connect(self.start_capture)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        # Capture frame-by-frame
        ret, frame = self.capture.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        self.num_of_faces = len(faces)

        # Crop and store first detected face
        if self.num_of_faces > 0:
            (x, y, w, h) = faces[0]
            self.current_image = frame[y: y + h, x: x + w]

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = resize_image(frame, self.cameraLabel.width(), self.cameraLabel.height())
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0],
                             QtGui.QImage.Format_RGB888)
        self.cameraLabel.setPixmap(QtGui.QPixmap.fromImage(image))

    def add_data(self, name):
        current_image = self.current_image
        num_of_faces = self.num_of_faces

        if not self.data_builder.standardized:
            self.data_builder.standardize()

        if num_of_faces > 0:
            self.data_builder.synchronize(current_image, name)
            return 1
        else:
            return 0

    def start_capture(self):
        self.startButton.setDisabled(True)
        name, ok = QtWidgets.QInputDialog.getText(self, "Enter Name", "Enter Your Name:")
        while name == '' or not ok:
            if name == '':
                name, ok = QtWidgets.QInputDialog.getText(self, "Enter Name",
                                                          "Name cannot be empty. Re-enter Your Name:")
            else:
                name, ok = QtWidgets.QInputDialog.getText(self, "Enter Name", "Enter Your Name:")
        self.name = name
        self.capture_thread.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = JHDataCollectorGUI()
    form.show()
    app.exec_()
