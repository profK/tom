import base64

from TomPluginManager import AppContext


class ImageStoreService():
    def __init__(self):
        global ctxt


        print("Loaded ImageStoreService")

    def init_service(self,appContext: AppContext):
        global ctxt, imageDB
        ctxt = appContext
        imageDB = ctxt.Data.OpenTable("Images")

    def exposed_store_image_bytes(self,key: str, imgdata: bytes)  -> bool:
        global imageDB
        try :
           xition = imageDB.begin_transaction()
           xition.put(key,imgdata.decode())
           xition.end()
           return True
        except BaseException as ex:
            print("Error storing image with key "+key)
            print(ex)
            return False

    def exposed_get_image_bytes(self,key: str) -> bytes :
        try :
           xition = imageDB.begin_transaction()
           imgdata = xition.get(key)
           xition.end()
           return imgdata.encode()
        except BaseException :
            print("Error getting image with key "+key)
            return None
