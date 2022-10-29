from PyQt6.QtGui import QAction
import os.path
from PyQt6 import uic

from TomPluginManager import AppContext

DEPENDENCIES = {
    "Window"
}
def OnButtonClick() :
        global dialog
        dialog.setVisible(True)

ToolBarAction = QAction("Account")
ToolBarAction.triggered.connect(OnButtonClick)

def init_plugin(ctxt: AppContext) :
    global dialog
    dialog = uic.loadUi(os.path.join(dir, "ConnectDialog.ui"))
    ctxt.Window.AddToToolbar(ToolBarAction)
    #TODO  Wire up dialog





