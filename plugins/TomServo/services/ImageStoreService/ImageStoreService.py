import base64
import inspect
import json
import os.path

from TomPluginManager import AppContext
from plugins.Data import Cursor
from datetime import datetime
from datetime import datetime

rootPath = os.path.dirname(__file__)

def save_image_to_file(key:str, imgdata:bytes) :
    path = key[0:key.rfind("."):]
    path = path.replace(",","/")
    if not os.path.exists(path) :
        os.makedirs(path)
    filename = key[key.rfind(".")+1::]
    path = os.path.join(rootPath,path,filename)
    with open(path, "wb") as binary_file:
        # Write bytes to file
        binary_file.write(imgdata)

def read_image_from_file(key:str) ->bytes :
    path = key[0:key.rfind("."):]
    path = path.replace(",", "/")
    filename = key[key.rfind(".") + 1::]
    path = os.path.join(rootPath, path, filename)
    with open(path, "rb") as binary_file:
        # read bytes from file
        return binary_file.read()

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
           xition.put(key,{"key":key,  "timestamp":datetime.utcnow()})
           save_image_to_file(os.path.join(rootPath,key),imgdata)
           xition.end()
           return True
        except BaseException as ex:
            print("Error storing image with key "+key)
            print(ex)
            return False

    def exposed_get_image_bytes(self,key: str) -> bytes :
        try :
           imgdata: bytes  = read_image_from_file(os.path.join(rootPath,key))
           return imgdata
        except BaseException :
            print("Error getting image with key "+key)
            return None

    def exposed_get_image_list(self,prfx: str) -> list :
        try:
            xition = imageDB.begin_transaction()
            cursor: Cursor = xition.cursor()
            imageData: list = list()
            foundStart: bool = False
            for kv in cursor :
                if kv == None :
                    break
                else :
                    key: str =kv["key"]
                    if key.startswith(prfx) :
                        imageData.append(kv["value"])
                    else :
                        if len(imageData)>0 :
                            break
            return imageData
        except BaseException as ex :
            print(ex)

    def exposed_clear_all_images(self) :
       imageDB.clearAll()

