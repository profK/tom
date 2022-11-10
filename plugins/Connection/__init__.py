from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QDialog
import rpyc
import os.path
from PyQt6 import uic
import hashlib
#fastAPI
from typing import Union
from fastapi import FastAPI
import imageio as iio


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

def set_dialog_connected(connected: bool) :
    dialog.hostname.setDisabled(connected)
    port = dialog.setDisabled(connected)
    user = dialog.setDisabled(connected)
    password = dialog.setDisabled(connected)

def connect_server() :
    global ctxt
    host = dialog.hostname.text()
    port = dialog.portnum.text()
    user = dialog.username.text()
    password = dialog.password.text()
    hash = hashlib.sha384(password.encode()).hexdigest()
    try:
        conn = rpyc.connect(host, int(port))
        if conn.root.login(user, hash):
            ctxt.Connection.conn = conn
            set_dialog_connected(True)
            ctxt.Window.ShowMessage("Connection Result",
                                    "You are connected to "+host+":"+port)

            close_dialog()
        else:
            ctxt.Window.ShowMessage("Connection Result",
                                    "Invalid user or password")
            close_dialog()
    except BaseException as ex:
        ctxt.Window.ShowMessage("Connection Result",
                                "Connection to " + host + ":" + port +" failed")
        close_dialog()
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



