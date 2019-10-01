from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(200, 200, 400, 400)
win.setWindowTitle("Mission Planer")
win.show()
sys.exit(app.exec_())
