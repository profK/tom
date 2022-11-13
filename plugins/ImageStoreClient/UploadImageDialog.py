import base64
import os
from PyQt6 import uic
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QFileDialog

from TomPluginManager import AppContext

rootdir = os.path.dirname(os.path.realpath(__file__))


def GetBiggestPixmapFromQIcon(icon: QIcon) -> QPixmap:
    sizes = icon.availableSizes()
    maximum: int = sizes[0].width();
    for size in sizes:
        maximum = max(maximum, size.width());

    return icon.pixmap(QSize(maximum, maximum));


def PixmapToByteArray(pixmap: QPixmap) -> bytes:
    image = pixmap.toImage()
    sz = image.sizeInBytes()
    bits = image.bits().asarray(sz)
    return bits

class UploadImageDialog :
    def __init__(self,prefix:str,ctxt:AppContext) :
        self.ctxt = ctxt
        self.gui = uic.loadUi(os.path.join(rootdir, "uploadImageDialog.ui"))
        self.gui.image.setIcon(QIcon(os.path.join(rootdir, "select_image.png")))
        self.gui.cancel.clicked.connect(self.close)
        self.gui.save.clicked.connect(self.save_new_image)
        self.gui.image.clicked.connect(self.choose_local_image)
        self.gui.prefix.setText(prefix)


    def close(self, val:bool = True):
        self.gui.done(val)

    def save_new_image(self):
        pixmap = GetBiggestPixmapFromQIcon(self.gui.image.icon())
        self.StoreImage(
            self.gui.prefix.text() + self.gui.name.text(),
            base64.b64encode(PixmapToByteArray(pixmap)))
        self.close()

    def choose_local_image(self):
        filename = QFileDialog.getOpenFileName(caption="Choose an image to uploade")
        if not filename == None:
            try:
                image = QPixmap(filename[0])
                self.gui.image.setIcon(QIcon(image))
                filebase = os.path.basename(filename[0])
                filebase = os.path.splitext(filebase)[0]
                self.gui.name.setText(filebase)
            except BaseException as ex:
                print("Error loading file: " + str(ex))


    def open(self):
        self.gui.exec()



    def StoreImage(self, key: str, image: QPixmap):
        data = base64.b64encode(image)
        self.ctxt.Connection.conn.root.ImageStoreService.store_image_bytes(key, data)

    def PopulateImageSelector(self, prefix: str):
        names = self.ctxt.Connection.conn.root.ImageStoreService.get_image_list(prefix)

        for name in names:
            print(name)
            pass
