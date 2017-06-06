import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget


# New class which is inheritance of QWidget
class QWidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)  # set position and size
        self.setWindowTitle('TestQt')
        self.center()
        icon = QIcon('../resources/icon/embarrass_icon.png')

        self.setWindowIcon(icon)

        self.setToolTip("This is <em>QWidget</em>")

        # create quit button
        qbtn = QPushButton(icon, 'Quit', self)
        qbtn.setToolTip("Quit Program")
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        # connect quit button's clicked signal to slot
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        # show widget
        self.show()

    # Move window to center;
    def center(self):
        tmpRetangle = self.frameGeometry()  # get a rectangle specifying the geometry of the main window
        centerPoint = QDesktopWidget().availableGeometry().center()  # get screen resolution then get center point
        tmpRetangle.moveCenter(centerPoint)  # set center of rectangle to center point of screen
        self.move(tmpRetangle.topLeft())  # move window to rectangle

    # Message box when close button clicked (not quit button)
    def closeEvent(self, event):
        replyQuit = QMessageBox.question(self, 'Message',
                                         "Are you sure to quit?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)

        if replyQuit == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':  # only exec if this file is called as main program
    app = QApplication(sys.argv)
    example = QWidgetExample()
    sys.exit(app.exec_())
