
from PyQt5.QtWidgets import *


app = QApplication([])
win = QWidget()

alert = QMessageBox()
alert.setText("FatherTouch")
alert.exec()

win.show()
app.exec()