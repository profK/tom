# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt6.QtWidgets import QApplication
import TomPluginManager



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("start")
    app = QApplication(sys.argv)
    pluginManager=TomPluginManager.PluginManager()
    pluginManager.load_plugins()
    ctxt = pluginManager.appContext
    ctxt.conn.root.TestProxy.ping()
    app.exec()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
