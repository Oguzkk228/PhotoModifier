from PyQt5.QtCore import Qt
import os
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageOps, ImageFilter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QFileDialog, QMessageBox
class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.image = None
        self.dir = None
        self.save_dir = 'Modified/'
    def LoadImage(self, filename):
        self.filename = filename
        self.dir = workdir
        image_path = os.path.join(self.dir, self.filename)
        self.image = Image.open(image_path)
    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width = pic.width()
        label_height = pic.height()
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        pic.setPixmap(scaled_pixmap)
        pic.setVisible(True)
    def saveImage(self):
            path = os.path.join(self.dir, self.save_dir)
            if not(os.path.exists(path) or os.path.isdir(path)):
                os.mkdir.path(path)
            image_path = os.path.join(path, self.filename)
            self.image.save(image_path)
    def do_bw(self):
        if spisok.selectedItems():
            self.image = ImageOps.grayscale(self.image)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('ВЫБЕРИТЕ КАРТИНКУ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            error_win.exec()
    def rotate_left(self):
        if spisok.selectedItems():
            self.image = self.image.rotate(90)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('ВЫБЕРИТЕ КАРТИНКУ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            error_win.exec()
    def rotate_right(self):
        if spisok.selectedItems():
            self.image = self.image.rotate(270)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('ВЫБЕРИТЕ КАРТИНКУ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            error_win.exec()
    def mirror(self):
        if spisok.selectedItems():
            self.image = ImageOps.mirror(self.image)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('ВЫБЕРИТЕ КАРТИНКУ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            error_win.exec()
    def shaprness(self):
        if spisok.selectedItems():
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            try:
                self.image = self.image.filter(ImageFilter.SHARPEN)
            except:
                error_win = QMessageBox()
                error_win.setText('к сожжжжжалению ваша картинка плохая, мне с ней мама запретила работать выберите другую1!')
                error_win.exec()
    def blur(self):
        if spisok.selectedItems():
            self.image = self.image.filter(ImageFilter.BLUR)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('ВЫБЕРИТЕ КАРТИНКУ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            error_win.exec()
workimage = ImageProcessor()
workdir = ''
def showChosenImage():
    if spisok.currentRow() >= 0:
        filename = spisok.currentItem().text()
        workimage.LoadImage(filename)
        image_path = os.path.join(workimage.dir, filename)
        workimage.showImage(image_path)
def chooseworkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files, extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result
def showfilenamesList():
    chooseworkDir()
    extensions = ['.jpg', '.jpeg', '.png', '.gif']
    files = os.listdir(workdir)
    files = filter(files, extensions)
    spisok.clear()
    spisok.addItems(files)
app = QApplication([])
main_win = QWidget()
main_win.resize(700, 500)
main_win.setWindowTitle('Easy Editor')
fail = QPushButton('Папка')
spisok = QListWidget()
pic = QLabel('Картинка')
Left = QPushButton('Лево')
btnBlur = QPushButton('Сгладить')
Right = QPushButton('Право')
Mirror = QPushButton('Зеркало')
sharpen = QPushButton('Резкость')
monochrome = QPushButton('Ч/Б')
leftVlayout = QVBoxLayout()
rightVlayout = QVBoxLayout()
MainHlayout = QHBoxLayout()
Hlayout = QHBoxLayout()
leftVlayout.addWidget(fail)
leftVlayout.addWidget(spisok)
rightVlayout.addWidget(pic)
Hlayout.addWidget(Left)
Hlayout.addWidget(Right)
Hlayout.addWidget(Mirror)
Hlayout.addWidget(sharpen)
Hlayout.addWidget(btnBlur)
Hlayout.addWidget(monochrome)
rightVlayout.addLayout(Hlayout)
MainHlayout.addLayout(leftVlayout)
MainHlayout.addLayout(rightVlayout)
main_win.setLayout(MainHlayout)
fail.clicked.connect(showfilenamesList)
monochrome.clicked.connect(workimage.do_bw)
Left.clicked.connect(workimage.rotate_left)
Right.clicked.connect(workimage.rotate_right)
Mirror.clicked.connect(workimage.mirror)
btnBlur.clicked.connect(workimage.blur)
spisok.currentRowChanged.connect(showChosenImage)
sharpen.clicked.connect(workimage.shaprness)
main_win.show()
app.exec()
