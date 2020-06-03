from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()
    def main(self):
        self.resize(400,400)
        self.btn = QPushButton("HI",self)
        self.btn.clicked.connect(self.go)
    def go(self):
        self.msg = QMessageBox()
        self.msg.setText("Hello")
        self.msg.exec()
app = QApplication([])
win = MyApp()
win.show()
app.exec();