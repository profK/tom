import base64

from PyQt6.QtGui import QPixmap

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



