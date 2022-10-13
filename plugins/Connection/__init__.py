from PyQt6.QtGui import QAction
import rpyc

from TomPluginManager import AppContext

global conn

def OnButtonClick() :
    print("Connection Button Clicked")

ToolBarAction = QAction("Connections")
ToolBarAction.triggered.connect(OnButtonClick)

def init_plugin(ctxt:AppContext) :
    global conn
    ctxt.Window.AddToToolbar(ToolBarAction)
    try:
        conn = rpyc.connect("localhost",18812)
        if conn.root.login("test","password") :
            print("connected to tomservo")
            ctxt.conn = conn
        else :
            print("Invalid user or password")
    except BaseException as ex :
        print("Connection failed: "+str(ex))
