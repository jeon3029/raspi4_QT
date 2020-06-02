#15반 전태준 0602 데일리 과제 2
from PyQt5.QtWidgets import *
        
app = QApplication([])
win = QWidget()

form = QFormLayout()
win.setLayout(form)

formEdit = QLineEdit()
sendButton = QPushButton("푸시버튼")
form.addRow("이름",formEdit)
form.addRow(sendButton)

win.show()
app.exec()