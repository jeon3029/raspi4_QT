from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

win.resize(500,500)
widget = QWidget()
label = QLabel("Think of Jjappaguri",widget)
label.adjustSize()
win.setCentralWidget(widget)

bar = win.statusBar()
bar.showMessage("I am hungry")

menu = win.menuBar()
menuMenu = menu.addMenu('Menu')
menuBye = menu.addMenu('Bye')

menu_1 = QAction("menu1",win)
menuMenu.addAction(menu_1)
menu_2 = QAction("menu2",win)
menuBye.addAction(menu_2)

win.show()
app.exec()