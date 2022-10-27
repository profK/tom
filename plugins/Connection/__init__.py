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
global ctxt

def OnButtonClick() :
    global dialog
    dialog.setVisible(True)

ToolBarAction = QAction("Connections")
ToolBarAction.triggered.connect(OnButtonClick)

def close_dialog() :
    dialog.setVisible(False)

def connect_server() :
    global ctxt
    host = dialog.hostname.text()
    port = dialog.portnum.text()
    try:
        conn = rpyc.connect(host, int(port))
        if conn.root.login("test", "password"):
            ctxt.Window.ShowMessage("Connection Result",
                                    "You are connected to "+host+":"+port)
            ctxt.Connection.conn = conn
            close_dialog()
        else:
            ctxt.Window.ShowMessage("Connection Result",
                                    "Invalid user or password")
    except BaseException as ex:
        ctxt.Window.ShowMessage("Connection Result",
                                "Connection to " + host + ":" + port +" failed")
    pass

def init_plugin(context:AppContext) :
    global conn, dialog, ctxt
    ctxt = context
    ctxt.Window.AddToToolbar(ToolBarAction)
    dir = os.path.dirname(__file__)
    dialog = uic.loadUi(os.path.join(dir,"ConnectDialog.ui"))
    dialog.closebutton.clicked.connect(close_dialog)
    dialog.connectbutton.clicked.connect(connect_server)
    ctxt.Window.AddToWindow(dialog)


