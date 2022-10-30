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


def select_icon() :
    ctxt.ImageStoreClient.ShowImageChooser("icons.")

def init_plugin(context: AppContext) :
    global dialog, ctxt
    ctxt = context
    dir = os.path.dirname(__file__)
    dialog = uic.loadUi(os.path.join(dir, "AccountDialog.ui"))
    defaultAvatar = QIcon(os.path.join(dir, "ClickToAddAvatar.png"))
    dialog.icon.setIcon(defaultAvatar)
    #wire thw controls
    dialog.icon.clicked.connect(select_icon)

    ctxt.Window.AddToToolbar(ToolBarAction)
    #TODO  Wire up dialog





