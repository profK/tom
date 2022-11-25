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
            self.gui.prefix.text
        )

        #write names and throw off threads to get pictures
        vLayout: QVBoxLayout = QVBoxLayout()
        currentLayout: QHBoxLayout = QHBoxLayout()
        for name in names :
            if currentLayout.count()==4 :
                hBoxWidget: QWidget = QWidget()
                hBoxWidget.setLayout(currentLayout)
                vLayout.addChildWidget(hBoxWidget)
                currentLayout: QHBoxLayout = QHBoxLayout()
            imageLayout: QVBoxLayout = QVBoxLayout()
            imageButton: QPushButton = QPushButton(imageLayout)
            imageButton.setIcon(imageLoadingPng)
            label: QLabel = QLabel(imageLayout,name)
            imageLayout.addChildWidget(imageButton)
            imageLayout.addChildWidget(label)
            imageWidget : QWidget = QWidget()
            imageWidget.setLayout(imageLayout)
            currentLayout.addChildWidget(imageWidget)
            #launch image fetch
            #todo
        #add last currentLayout
        hBoxWidget: QWidget = QWidget()
        hBoxWidget.setLayout(currentLayout)
        vLayout.addChildWidget(hBoxWidget)
        contentsWidget: QWidget = QWidget()
        contentsWidget.setLayout(vLayout)
        self.gui.scrollArea.setWidget(contentsWidget)

