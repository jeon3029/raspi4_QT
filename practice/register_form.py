from PyQt5.QtWidgets import *

app = QApplication([])
win = QWidget()

form = QFormLayout()
win.setLayout(form)

formEdit1 = QLineEdit()
form.addRow("name",formEdit1)

formEdit2 = QLineEdit()
formButton = QPushButton("check age")

formLayout = QHBoxLayout()
formLayout.addWidget(formEdit2)
formLayout.addWidget(formButton)
form.addRow("age",formLayout)
formLabel = QLabel("Warning : too much age")
form.addWidget(formLabel)

formLabel.setVisible(False)
formButton2 = QPushButton("Register")
form.addRow(formButton2)

def checkAge():
    age = formEdit2.text()
    if age.isdigit() == False:
        formLabel.setText("Warning : not integer")
        formLabel.setVisible(True)
        return
    formLabel.setText("Warning : too much age")
    
    age = int(age)
    if age>= 25:
        formLabel.setVisible(True)
    else:
        formLabel.setVisible(False)
def checkName():
    name = formEdit1.text()
    n = len(name)
    if 1<=n<=4 : pass
    else:
        msg = QMessageBox()
        msg.setText("name must 1-4 length")
        msg.exec()
        
formButton.clicked.connect(checkAge)
formButton2.clicked.connect(checkName)

app.setApplicationName("My World")

win.show()
app.exec_()