from PyQt6.QtGui import QAction

from TomPluginManager import AppContext

DEPENDENCIES = {
    "Window"
}
def OnButtonClick() :
    print("Dummy Button Clicked")

ToolBarAction = QAction("Dummy")
ToolBarAction.triggered.connect(OnButtonClick)

def init_plugin(ctxt: AppContext) :
    ctxt.Window.AddToToolbar(ToolBarAction)





