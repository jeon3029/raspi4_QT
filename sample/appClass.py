
from PyQt5.QtWidgets import *

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,400,500)
        self.btn = QPushButton("Hello",self)
        self.btn.move(100,200)
        
app = QApplication([])
win = Form()
win.show()
app.exec()