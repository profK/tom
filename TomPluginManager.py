# A singleton module
import importlib
import os
from types import ModuleType

global plugins

#holds plugins
class AppContext(object) :
    def addManager(self,name:str,module:ModuleType) :
        self.__setattr__(name,module)

class PluginManager:
    def load_plugins( self,pluginDirectory: str="plugins") :
        global appContext
        appContext = AppContext()
        for file in os.listdir(pluginDirectory):
            d = os.path.join(pluginDirectory, file)
            if os.path.isdir(d) :
                mod = importlib.import_module(d.replace("\\","."))
                appContext.addManager(os.path.basename(d),mod)
        for attributeName in vars(appContext):
            if not attributeName.startswith("_"):
                print("init: "+attributeName)
                try:
                    mod = getattr(appContext,attributeName)
                    mod.init_plugin(appContext)
                except AttributeError as ex:
                    # warn has no init
                    print(ex)
                    print("Warning: cannot find init_plugin in plugin module " + file)
                except BaseException as ex:
                    # log exception
                    print(ex)




