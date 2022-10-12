from PyQt6.QtGui import QAction

from TomPluginManager import AppContext
from . import tomservo
import threading

def OnButtonClick() :
    print("Tomservo Button Clicked")

ToolBarAction = QAction("TomServo")
ToolBarAction.triggered.connect(OnButtonClick)

def init_plugin(ctxt: AppContext) :
    ctxt.Window.AddToToolbar(ToolBarAction)

threading.Thread(target=tomservo.start).start()