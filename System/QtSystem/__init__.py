import sys
from TomPluginManager import AppContext
from PyQt6.QtWidgets import QApplication

global app
app: QApplication = None
#In this callback goes all initialization that must happen before dependant plugis are loaded
def system_init(appContext: AppContext) :
    global app
    app = QApplication(sys.argv)

#This callback is alled after all plugins ahve been intiailized
#Its main use is to start the system input loop
def system_start(appContext: AppContext) :
    global app
    app.exec()
