import os
import time

import rpyc
from rpyc.utils.helpers import classpartial
from rpyc.core import netref
from rpyc.lib import get_methods, get_id_pack
import _thread
from rpyc.utils.server import ThreadedServer # or ForkingServer
from . import TomPluginManager

class TestProxy():
    def __init__(self):
        print(__class__)
    def exposed_ping(self):
        print("ping from "+__file__)




class MainService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_login(self,name:str,passwdHash:str) -> bool:
        xtion = userDB.begin_transaction()
        hash=xtion.get(name+".pwhash")
        xtion.end()
        return passwdHash==hash

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

# Load plugins
pluginsDir = os.path.join(os.path.dirname(__file__),"plugins")
pluginsDir = pluginsDir[len(os.getcwd())+1::]
pluginManager = TomPluginManager.PluginManager()
pluginManager.load_plugins(pluginsDir)
#load services
servicesDir = os.path.join(os.path.dirname(__file__),"services")
servicesDir = servicesDir[len(os.getcwd())+1::]
servicesManager = TomPluginManager.PluginManager()
servicesManager.load_plugins(servicesDir)
#register services
for serviceInit in servicesManager.get_all_plugins() :
    if hasattr(serviceInit,"SERVICES") :
        for kv in serviceInit.SERVICES :
            instance = kv[1]()
            print("TomServo found service: "+kv[0])
            setattr(MainService, "exposed_" + kv[0], instance)
#open database
userDB = pluginManager.appContext.Data.OpenTable("Users")
xtion = userDB.begin_transaction()
#mamke sure test login in there
if (not xtion.has("test.pwhash")) :
    xtion.put("test.pwhash","password")
xtion.end()

if __name__ == "__main__":
    start()

