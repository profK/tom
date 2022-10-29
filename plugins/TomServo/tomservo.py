import os
import time
import hashlib
import rpyc
from rpyc.utils.helpers import classpartial
from rpyc.core import netref
from rpyc.lib import get_methods, get_id_pack
import _thread
from rpyc.utils.server import ThreadedServer # or ForkingServer

from TomPluginManager import AppContext
from . import TomPluginManager

class TestProxy():
    def __init__(self):
        print(__class__)
    def exposed_ping(self):
        print("ping from "+__file__)

def set_user(db, name: str, password: str ) :
    xtion = db.begin_transaction()
    hash =  hashlib.sha384(password.encode()).hexdigest()
    xtion.put(name+"pwhash",hash)
    xtion.end()

def check_user(db,name: str,hash: str) -> bool :
    try :
        xtion = db.begin_transaction()
        dbhash= xtion.get(name + "pwhash")
        xtion.end()
        return dbhash==hash
    except BaseException as ex:
        print("DB exception: "+ex)
        return False

class MainService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        self.conn=conn
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        self.conn = None
        pass

    def exposed_login(self,name:str,passwdHash:str) -> bool:
        global userDB
        if check_user(userDB,name,passwdHash) :
            servicesManager.appContext.username = name
            return True
        else :
            servicesManager.appContext.username = name = None
            return False

    #exposed_TestProxy = TestProxy()

def start(host:str="localhost", port:int = 18812) :
    try :
        #pname = str(TestProxy.__name__)
        #for proxiedClass in {TestProxy}:
        #    pname = str(proxiedClass.__name__)
        #    setattr(MainService, "exposed_" + pname, proxiedClass())
        server = ThreadedServer(MainService,hostname=host, port=port)
        print("Tomservo is listening on " + host + ":" + str(port))
        server.start()

    except BaseException as ex :
        print(ex)
#make global appContext
appContext = AppContext()

# Load plugins
pluginsDir = os.path.join(os.path.dirname(__file__),"plugins")
pluginsDir = pluginsDir[len(os.getcwd())+1::]
pluginManager = TomPluginManager.PluginManager(appContext)
pluginManager.load_plugins(pluginsDir)
#load services
servicesDir = os.path.join(os.path.dirname(__file__),"services")
servicesDir = servicesDir[len(os.getcwd())+1::]
servicesManager = TomPluginManager.PluginManager(appContext)
servicesManager.load_plugins(servicesDir)
#register services
for serviceInit in servicesManager.get_all_plugins() :
    if hasattr(serviceInit,"SERVICES") :
        for kv in serviceInit.SERVICES :
            instance = kv[1]()
            instance.init_service(servicesManager.appContext)
            print("TomServo found service: "+kv[0])
            setattr(MainService, "exposed_" + kv[0], instance)
#open database
userDB = pluginManager.appContext.Data.OpenTable("Users")
set_user(userDB, "test","password")

if __name__ == "__main__":
    start()

