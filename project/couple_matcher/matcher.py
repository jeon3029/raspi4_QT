from PyQt5.QtWidgets import *
from PyQt5.uic import *
import hashlib
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("design.ui",self)
    def bye(self):
        self.close()
    def check(self):
        print(self.textBox1.text())
        str1 = self.textBox1.text()
        print(self.textBox2.text())
        str2 = self.textBox2.text()
        hashCode1 = hashlib.sha256(str1.encode()).hexdigest()
        hashCode2 = hashlib.sha256(str2.encode()).hexdigest()
        
        result = int(hashCode1,16) + int(hashCode2,16)
        result = result + (777 * self.spinBox.value())
        result = result % 101
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Warning Warning")
        msg.setText("Nasa 공식에 의해, " + str(result) + "%  확률로 커플이 됩니다.")
        msg.exec()
        print("CHECK")
    def clear(self):
        self.textBox1.setText("")
        self.textBox2.setText("")
        self.spinBox.setValue(20)
        print("CLEAR")
app = QApplication([])
win = MyApp()
win.show()
app.exec()