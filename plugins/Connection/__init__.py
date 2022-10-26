from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QDialog
import rpyc
import os.path
from PyQt6 import uic


from TomPluginManager import AppContext

DEPENDENCIES = {
    "Window"
}


global conn
global dialog
def OnButtonClick() :
    global dialog
    dialog.setVisible(True)

ToolBarAction = QAction("Connections")
ToolBarAction.triggered.connect(OnButtonClick)


def init_plugin(ctxt:AppContext) :
    global conn, dialog
    ctxt.Window.AddToToolbar(ToolBarAction)
    dir = os.path.dirname(__file__)
    dialog = uic.loadUi(os.path.join(dir,"ConnectDialog.ui"))
    ctxt.Window.AddToWindow(dialog)

    try:
        conn = rpyc.connect("localhost",18812)
        if conn.root.login("test","password") :
            print("connected to tomservo")
            ctxt.Connection.conn = conn
        else :
            print("Invalid user or password")
    except BaseException as ex :
        print("Connection failed: "+str(ex))
