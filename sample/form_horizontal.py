
from PyQt5.QtWidgets import *


app = QApplication([])
win = QWidget()

win.setWindowTitle("HI")


lineEdit = QLineEdit(win)
button = QPushButton("HUHU",win)

mainLayout = QHBoxLayout()
mainLayout.addWidget(lineEdit)
mainLayout.addWidget(button)
win.setLayout(mainLayout)

win.show()
app.exec()