from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import numpy
import cv2


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("design.ui",self)
        self.main()
    def main(self):
        self.img = cv2.imread("../chip.jpg")
        self.img = self.processingImage(self.img)
        self.printImage(self.img,self.pic)
    def processingImage(self,img):
        return img
    def type0(self):
        img = self.img
        self.printImage(self.img,self.pic)
    def type1(self):
        img = self.img
        img = cv2.blur(img,(55,55))
        self.printImage(img,self.pic)
    def type2(self):
        img = self.img
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        self.printImage(img,self.pic)
    def type3(self):
        img = self.img
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        kernel = numpy.ones((3,3),numpy.uint8)
        img = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
        self.printImage(img,self.pic)
    def type4(self):
        img = self.img
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,img = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
        self.printImage(img,self.pic)
    def type5(self):
        img = self.img
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = cv2.Canny(img,50,200)
        self.printImage(img,self.pic)

    def printImage(self,imgBGR,pic):
        imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)
        h,w,byte = imgRGB.shape
        img = QImage(imgRGB,w,h,byte*w,QImage.Format_RGB888)
        pic.setPixmap(QPixmap(img))

app = QApplication([])
win = MyApp()
win.show()
app.exec()