from PyQt5.QtWidgets import *
def hi():
    msg = QMessageBox()
    msg.setText(edit.text())
    msg.exec_()
app = QApplication([])
win = QWidget()
button = QPushButton("HI",win)
button.clicked.connect(hi)

edit = QLineEdit(win)

layout = QVBoxLayout()
layout.addWidget(edit)
layout.addWidget(button)

win.setLayout(layout)
win.show()

app.exec()