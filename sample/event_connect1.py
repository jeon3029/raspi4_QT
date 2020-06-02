from PyQt5.QtWidgets import *
        
app = QApplication([])
button = QPushButton('Click')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText("You clicked Button!")
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec()