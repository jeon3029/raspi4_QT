from PyQt5.QtWidgets import *

        
app = QApplication([])
window = QWidget()
mainlayout = QVBoxLayout()
headlayout = QHBoxLayout()
bodylayout = QVBoxLayout()

mainlayout.addLayout(headlayout)
mainlayout.addLayout(bodylayout)

headlayout.addWidget(QPushButton('One'))
headlayout.addWidget(QPushButton('TWO'))
headlayout.addWidget(QPushButton('THREE'))

bodylayout.addWidget(QPushButton('ONE'))
bodylayout.addWidget(QPushButton('TWO'))
bodylayout.addWidget(QPushButton('THREE'))


window.setLayout(mainlayout)
window.show()
app.exec()

