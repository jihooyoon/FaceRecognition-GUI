import sys
import cv2
# import qimage2ndarray
from PyQt5 import QtWidgets, QtGui, QtCore

import global_variables
import data_builder
import recognizer
from UI import mainwidget


def resize_image(src, width, height):
    src_height, src_width = src.shape[:2]
    factor_width = width / src_width
    factor_height = height / src_height
    if src_height * factor_width > height:
        factor = factor_height
    else:
        factor = factor_width
    return cv2.resize(src, (int(factor * src_width), int(factor * src_height)), interpolation=cv2.INTER_CUBIC)


class JHFaceGUI(QtWidgets.QWidget, mainwidget.Ui_mainForm):
    def __init__(self, parent=None):
        super(JHFaceGUI, self).__init__(parent)

        self.data_builder = data_builder.DataBuilder(global_variables.DATA_PATH)
        self.face_cascade = cv2.CascadeClassifier(global_variables.CASCADE_PATH)
        self.num_of_faces = 0
        self.recognizer = recognizer.Recognizer(self.data_builder, recognizer.FACE_RECOGNIZER_LBPH)
        self.recognizer_enable = False

        self.setupUi(self)
        self.nameLineEdit.setText('')

        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.cameraLabel.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cameraLabel.height())

        _, self.current_image = self.capture.read()
        self.addDataButton.clicked.connect(self.add_data)
        self.trainButton.clicked.connect(self.train)
        self.recognizeButton.clicked.connect(self.toggle_recognizer)
        self.thresholdLineEdit.textChanged.connect(self.set_threshold)

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
            if self.recognizer_enable:
                predicted = self.recognizer.predict(gray[y: y + h, x: x + w])
                cv2.putText(frame, predicted, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the resulting frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = resize_image(frame, self.cameraLabel.width(), self.cameraLabel.height())
        # image = qimage2ndarray.array2qimage(frame)
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0],
                             QtGui.QImage.Format_RGB888)
        self.cameraLabel.setPixmap(QtGui.QPixmap.fromImage(image))

    def add_data(self):
        self.addDataButton.setDisabled(True)
        name = self.nameLineEdit.text()
        current_image = self.current_image
        num_of_faces = self.num_of_faces

        if not self.data_builder.standardized:
            self.data_builder.standardize()
        if name == '':
            msg = QtWidgets.QMessageBox()
            msg.setText("Name is empty. Enter name before add image")
            msg.setWindowTitle("Message")
            retval = msg.exec_()
        elif num_of_faces <= 0:
            msg = QtWidgets.QMessageBox()
            msg.setText("No face detected")
            msg.setWindowTitle("Message")
            retval = msg.exec_()
        else:
            self.data_builder.synchronize(current_image, name)
            self.statusLabel.setText(name + '\'s face is added')

            self.capturedLabel.setStyleSheet("background: rgb(128, 128, 128); padding: 0")
            current_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
            current_image = resize_image(current_image, self.capturedLabel.width(), self.capturedLabel.height())
            # image = qimage2ndarray.array2qimage(frame)
            image = QtGui.QImage(current_image, current_image.shape[1], current_image.shape[0],
                                 current_image.strides[0], QtGui.QImage.Format_RGB888)
            self.capturedLabel.setPixmap(QtGui.QPixmap.fromImage(image))

        self.addDataButton.setDisabled(False)

    def train(self):
        self.trainButton.setDisabled(True)
        self.recognizer.train()
        if not self.recognizer.is_trained:
            msg = QtWidgets.QMessageBox()
            msg.setText("Training data is empty")
            msg.setWindowTitle("Message")
            retval = msg.exec_()
        self.trainButton.setDisabled(False)

    def toggle_recognizer(self):
        if not self.recognizer_enable:
            if not self.recognizer.is_trained:
                msg = QtWidgets.QMessageBox()
                msg.setText("Recognizer is not trained or training data is empty")
                msg.setWindowTitle("Message")
                retval = msg.exec_()
            else:
                self.recognizer_enable = True
                self.recognizeButton.setText("STOP RECOGNIZING")
        else:
            self.recognizer_enable = False
            self.recognizeButton.setText("RECOGNIZE")

    def set_threshold(self):
        threshold_str = self.thresholdLineEdit.text()
        try:
            threshold = float(threshold_str)
            self.recognizer.set_threshold(threshold)
        except ValueError:
            print("Threshold input text is not a float")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = JHFaceGUI()
    form.show()
    app.exec_()
