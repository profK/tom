import os.path

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtGui import QAction

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dir = os.path.dirname(__file__)
        self.window = uic.loadUi(os.path.join(dir,"mainwindow.ui"), self)
        self.toolbar: QtWidgets.QToolBar = self.window.toolBar;

    def add_to_toolbar(self,action:QAction) :
        self.toolBar.addAction(action)

    def add_to_window(self,widget: QWidget) :
        widget.parent = self.window




