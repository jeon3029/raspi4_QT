# OpenCV with RaspberryPi

## 사전 필요 Package 및 모듈
- 카메라
```sh
# 카메라 테스트
$ raspistill -o test.jpg # 해당 사진파일 열어봐서 제대로 찍히는지 확인
```
- OpenCV 설치
```sh
# 설치 script
$ sudo apt-get update 
$ sudo apt-get -y install build-essential cmake pkg-config 
$ sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
$ sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get -y install libxvidcore-dev libx264-dev
$ sudo apt-get -y install libfontconfig1-dev libcairo2-dev
$ sudo apt-get -y install libgdk-pixbuf2.0-dev libpango1.0-dev
$ sudo apt-get -y install libgtk2.0-dev libgtk-3-dev

$ sudo apt-get -y install libatlas-base-dev gfortran
$ sudo apt-get -y install libhdf5-dev libhdf5-serial-dev libhdf5-103
$ sudo apt-get -y install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
$ pip3 install imutils
$ pip3 install opencv-contrib-python==4.1.0.25
```