# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt6.QtWidgets import QApplication
import os
import TomPluginManager
import importlib


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("start")
    systemModules: list = os.listdir("System")
    if len(systemModules)==0 :
        print("Couldn't find a system module!")
        exit(1)
    #otherwise use first one found as system module
    systemModule = importlib.import_module(
        os.path.join("System",systemModules[0]).replace("\\","."))
    appContext = TomPluginManager.AppContext()
    appContext.System=systemModule
    appContext.System.system_init(appContext)
    pluginManager=TomPluginManager.PluginManager(appContext)
    pluginManager.load_plugins()
    appContext.System.system_start(appContext)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
