import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget
from PyQt6.uic.properties import QtWidgets

from TomPluginManager import AppContext
from . import MainWindow
__window = MainWindow.MainWindow()

def AddToToolbar(action: QAction):
    __window.add_to_toolbar(action)

def AddToWindow(widget: QWidget):
    __window.add_to_toolbar(widget)

def init_plugin(ctx:AppContext):
    __window.show()

