import base64
import os

from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QFileDialog

from TomPluginManager import AppContext

DEPENDENCIES = {

}


#ToolBarAction = QAction("Dummy Button")
#ToolBarAction.triggered.connect(OnButtonClick)

def init_plugin(appContext: AppContext) :
    global ctxt
    ctxt = appContext

def StoreImage(key: str, image: QPixmap) :
    global ctxt
    data = base64.b64encode(image)
    ctxt.conn.root.ImageStoreService.store_image_bytes(key, data)

def GetImage(key:str) -> QPixmap :
    global ctxt
    imgData = ctxt.conn.root.ImageStoreService.get_image_bytes(key)
    if imgData == None :
        return None
    else :
        return base64.b64decode(imgData)

def ShowImageChooser(prefix: str) -> str :
     global imageSelector
     uploadImageDialog.prefix.setText(prefix)
     imageSelector.prefix.setText(prefix)
     imageSelector.exec()

def upload_image() :
    #fileName = QFileDialog.getOpenFileName(caption="Upload an image")
    #if not fileName == None :
        #pixmap = QPixmap(fileName)
    uploadImageDialog.exec()

def close_image_selector() :
    imageSelector.setVisible(False)

def close_save_dialog() :
    uploadImageDialog.setVisible(False)

def save_new_image():
    uploadImageDialog.setVisible(False)

def choose_local_image() :
    filename = QFileDialog.getOpenFileName(caption="Choose an image to uploade")
    if not filename==None :
        try :
            image = QPixmap(filename[0])
            uploadImageDialog.image.setIcon(QIcon(image))
            filebase = os.path.basename(filename[0])
            filebase = os.path.splitext(filebase)[0]
            uploadImageDialog.name.setText(filebase)
        except BaseException as ex:
            print("Error loading file: "+str(ex))

dir = os.path.dirname(__file__)
imageSelector = uic.loadUi(os.path.join(dir,"ImageSelectDialog.ui"))
imageSelector.upload.clicked.connect(upload_image)
#imageSelector.cancel.clicked.connect(close_image_selector)

uploadImageDialog = uic.loadUi(os.path.join(dir,"uploadImageDialog.ui"))
uploadImageDialog.image.setIcon(QIcon(os.path.join(dir, "select_image.png")))
uploadImageDialog.cancel.clicked.connect(close_save_dialog)
uploadImageDialog.save.clicked.connect(save_new_image)
uploadImageDialog.image.clicked.connect(choose_local_image)

