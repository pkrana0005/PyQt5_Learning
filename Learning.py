from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(200, 200, 400, 400)
win.setWindowTitle("Mission Planer")

label = QtWidgets.QLabel(win)
label.setText("my first label")
label.move(50, 50)

win.show()
sys.exit(app.exec_())
