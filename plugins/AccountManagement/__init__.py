from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction,QIcon
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
    dir = os.path.dirname(__file__)
    dialog = uic.loadUi(os.path.join(dir, "AccountDialog.ui"))
    defaultAvatar = QIcon(os.path.join(dir, "ClickToAddAvatar.png"))
    dialog.icon.setIcon(defaultAvatar)

    ctxt.Window.AddToToolbar(ToolBarAction)
    #TODO  Wire up dialog





