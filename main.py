from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6 import uic
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('gui.ui',self)
def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
