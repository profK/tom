import os

from PyQt6 import uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QLabel

from TomPluginManager import AppContext
from .UploadImageDialog import UploadImageDialog

rootdir = os.path.dirname(os.path.realpath(__file__))

imageLoadingPng =  QIcon(os.path.join(rootdir, "LoadingImage.png"))

class ImageSelectDialog :
    def __init__(self,prefix: str,ctxt:AppContext):
        self.ctxt=ctxt
        self.gui = uic.loadUi(os.path.join(rootdir, "ImageSelectDialog.ui"))
        self.gui.upload.clicked.connect(self.upload_image)
        self.uploadImageDialog = UploadImageDialog(prefix,ctxt)
        self.gui.prefix.setText(prefix)

    def upload_image(self):
        self.uploadImageDialog.open()

    def open(self) :
        self.populate()
        self.gui.exec()

    def clearImageButtons(self) :
        parentWidget = self.gui.scrollArea.contents.verticalLayout
        while parentWidget.count():
            child = parentWidget.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def populate(self):
        names = self.ctxt.Connection.conn.root.ImageStoreService.get_image_list(
            self.gui.prefix.text
        )
        self.clearImageButtons()
        #write names and throw off threads to get pictures
        vLayout: QVBoxLayout = self.gui.scrollArea.contents.verticalLayout
        currentLayout: QHBoxLayout = QHBoxLayout(vLayout)
        for name in names :
            if currentLayout.count()==4 :
                currentLayout: QHBoxLayout = QHBoxLayout(vLayout)
            imageLayout: QVBoxLayout = QVBoxLayout(currentLayout)
            imageButton: QPushButton = QPushButton(imageLayout)
            imageButton.setIcon(imageLoadingPng)
            label: QLabel = QLabel(imageLayout,name)
            #launch image fetch
            #todo

