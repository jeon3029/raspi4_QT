from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
#close action
class MainWindow(QMainWindow):
    def closeEvent(self,e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(window,None,"SAVE or NOT",
            QMessageBox.Save|
            QMessageBox.Discard|
            QMessageBox.Cancle
            )
        if answer & QMessageBox.Save:
            save()
        elif answer & QMessageBox.Cancle:
            e.ignore()

app = QApplication([])
app.setApplicationName("Notepad")
text = QPlainTextEdit()

#File Menu
window = MainWindow()
window.setCentralWidget(text)
menu = window.menuBar().addMenu("&File")
#Open File
open_action = QAction("&Open")
def open_file():
    path = QFileDialog.getOpenFileName(window,"Open File")[0]
    if path:
        text.setPlainText(open(path).read())
open_action.triggered.connect(open_file)
#ctrl + o to open
open_action.setShortcut(QKeySequence("Ctrl+O"))
menu.addAction(open_action)

#Save File
save_as_action = QAction("Save &As...")
##ctrl + s
file_path = None
save_action = QAction("&Save")
def save():
    if file_path is None:
        save_as()
    else:
        with open(file_path,"w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)
save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence("Ctrl+S"))
menu.addAction(save_action)
def save_as():
    global file_path
    path = QFileDialog.getOpenFileName(window,"Save As")[0]
    if path:
        file_path = path
        save()
save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)
#Close Menu
close = QAction("&Close")
close.triggered.connect(window.close)
menu.addAction(close)

#Help Menu
help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
help_menu.addAction(about_action)
## help menu dialog
def show_about_dialog():
    about_text = "<center>"\
    "<h1>Text Editor"\
    "</center>"\
    "<p>Version 1.0.0<br>"\
    "Copyright taejjeon</p>"
    QMessageBox.about(window,"About",about_text)
about_action.triggered.connect(show_about_dialog)

window.show()
text.show()
app.exec()