import sys

from PyQt6.QtGui import QAction
from PyQt6.uic.properties import QtWidgets

from TomPluginManager import AppContext
from . import MainWindow
__window = MainWindow.MainWindow()

def AddToToolbar(action: QAction):
    __window.add_to_toolbar(action)

def init_plugin(ctx:AppContext):
    __window.show()

