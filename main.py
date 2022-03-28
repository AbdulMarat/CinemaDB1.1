from gui import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

qapp = QApplication(sys.argv)
window = MainWindow()
window.show()
qapp.exec()

