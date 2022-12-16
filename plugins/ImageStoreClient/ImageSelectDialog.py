import os

from PyQt6 import uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QWidget

from TomPluginManager import AppContext
from .UploadImageDialog import UploadImageDialog


rootdir = os.path.dirname(os.path.realpath(__file__))

imageLoadingPng =  QIcon(os.path.join(rootdir, "LoadingImage.png"))


class ImageSelectDialog :
    def __init__(self,prefix: str,ctxt:AppContext):
        self.ctxt=ctxt
        self.gui = uic.loadUi(os.path.join(rootdir, "ImageSelectDialog.ui"))
        from plugins.ImageStoreClient.ImageGallery import ImageGallery
        self.imageGallery:ImageGallery = ImageGallery()
        self.gui.scrollArea.setWidget(self.imageGallery);
        self.gui.upload.clicked.connect(self.upload_image)
        self.uploadImageDialog = UploadImageDialog(prefix,ctxt)
        self.gui.prefix.setText(prefix)

    def upload_image(self):
        self.uploadImageDialog.open()

    def open(self) :
        self.populate()
        self.gui.exec()


    def populate(self):
        names = self.ctxt.Connection.conn.root.ImageStoreService.get_image_list(
            self.gui.prefix.text()
        )

        for name in names :

        self.imageGallery.populate(picList, size)
        self.gui.repaint()
