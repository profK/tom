import base64
import inspect
import os.path

from TomPluginManager import AppContext
from plugins.Data import Cursor
from datetime import datetime

rootPath = os.path.dirname(inspect.getfile(inspect))

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
    fullnameNoExt = key[0:key.rfind("."):]
    path = fullnameNoExt[0:key.rfind("."):]
    path = path.replace(",","/")
    filename = key[key.rfind(".")::]
    with open(path+"/"+filename, "rb") as binary_file:
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
           save_image_to_file(key,imgdata)
           xition.end()
           return True
        except BaseException as ex:
            print("Error storing image with key "+key)
            print(ex)
            return False

    def exposed_get_image_bytes(self,key: str) -> bytes :
        try :
           imgdata: bytes  = read_image_from_file(key)
           return imgdata.encode()
        except BaseException :
            print("Error getting image with key "+key)
            return None

    def exposed_get_image_list(self,prefix: str) -> object :
        xition = imageDB.begin_transaction()
        cursor: Cursor = xition.cursor()
        imageData: list = list()
        foundStart: bool = False
        for kv in cursor :
            if kv == None :
                break
            else :
                if kv["key"].startswith(prefix) :
                    imageData.append(kv)
                else :
                    if len(imageData)>0 :
                        break
        return imageData

    def exposed_clear_all_images(self) :
       imageDB.clearAll()

