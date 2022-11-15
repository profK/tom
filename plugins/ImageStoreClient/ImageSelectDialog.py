import os

from PyQt6 import uic

from TomPluginManager import AppContext
from .UploadImageDialog import UploadImageDialog
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QLabel

rootdir = os.path.dirname(os.path.realpath(__file__))

class ImageButton(QVBoxLayout) :
    def __init__(self,id:str) :
        self.button = QPushButton()
        self.addWidget(self.button)
        self.label = QLabel(id)
        self.addWidget(self.label)

class ImageRow(QHBoxLayout):
    def __init__(self,imagesPerRow:int) :
        super().__init__()
        self.imagesPerRow = imagesPerRow
        self.imageCount=0

    def add_image(self,id:str) :
        self.addWidget(ImageButton(id))
        self.imageCount += 1

    def is_full(self) :
        return self.imageCount >= self.imagesPerRow



class ImageSelectDialog :
    def __init__(self,prefix: str,ctxt:AppContext):
        self.gui = uic.loadUi(os.path.join(rootdir, "ImageSelectDialog.ui"))
        self.gui.upload.clicked.connect(self.upload_image)
        self.uploadImageDialog = UploadImageDialog(prefix,ctxt)
        self.gui.prefix.setText(prefix)
        self.lastRow = self.make_new_row(4)

    def make_new_row(self,numPerRow:int) :
        return ImageRow(numPerRow)
    def upload_image(self):
        self.uploadImageDialog.open()

    def open(self) :
        self.clearImages()
        self.populate()
        self.gui.exec()

    def clearImages(self) :
        while self.gui.scrollArea.rows.count():
            child = self.gui.scrollArea.rows.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    def populate(self):
        global ctxt

        names = ctxt.Connection.conn.root.ImageStoreService.get_image_list(
            self.gui.prefix.text
        )

        for name in names :
            if self.lastRow.is_full() :
                self.lastRow = self.make_new_row(4)
            self.lastRow.add_image(name)
