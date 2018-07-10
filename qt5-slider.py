import sys

from PyQt5.QtWidgets import QApplication, QSlider, QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("qt5 with python")
        self.setGeometry(0, 0, 512, 512)

        # center window on desktop
        rectangle = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center)
        self.move(rectangle.topLeft())

        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(16)
        slider.setSingleStep(1)

        self.setCentralWidget(slider)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()