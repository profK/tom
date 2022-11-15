import os

from PyQt6 import uic

from TomPluginManager import AppContext
from .UploadImageDialog import UploadImageDialog

rootdir = os.path.dirname(os.path.realpath(__file__))

class ImageSelectDialog :
    def __init__(self,prefix: str,ctxt:AppContext):
        self.gui = uic.loadUi(os.path.join(rootdir, "ImageSelectDialog.ui"))
        self.gui.upload.clicked.connect(self.upload_image)
        self.uploadImageDialog = UploadImageDialog(prefix,ctxt)
        self.gui.prefix.setText(prefix)

    def upload_image(self):
        self.uploadImageDialog.open()

    def open(self) :
        self.gui.exec()

    def populate(self):
        global ctxt
        names = ctxt.Connection.conn.root.ImageStoreService.get_image_list(
            self.gui.prefix.text
        )

        for name in names:
            print(name)
            pass

