import base64
import os

from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QBuffer, QSize, QByteArray

from TomPluginManager import AppContext
from .ImageSelectDialog import ImageSelectDialog

DEPENDENCIES = {

}


#ToolBarAction = QAction("Dummy Button")
#ToolBarAction.triggered.connect(OnButtonClick)

def init_plugin(appContext: AppContext) :
    global ctxt
    ctxt = appContext
    ctxt.Connection.conn.root.ImageStoreService.clearAll() # for debugging



def GetImage(key:str) -> QPixmap :
    global ctxt
    imgData = ctxt.Connection.conn.root.ImageStoreService.get_image_bytes(key)
    if imgData == None :
        return None
    else :
        return base64.b64decode(imgData)


def ShowImageChooser(prefix: str) -> str :
    global ctxt
    ImageSelectDialog(prefix,ctxt).open()

dir = os.path.dirname(__file__)


#imageSelector.cancel.clicked.connect(close_image_selector)




