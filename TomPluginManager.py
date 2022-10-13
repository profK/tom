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
        self.appContext = AppContext()
        for file in os.listdir(pluginDirectory):
            d = os.path.join(pluginDirectory, file)
            if os.path.isdir(d) :
                mod = importlib.import_module(d.replace("\\","."))
                self.appContext.addManager(os.path.basename(d),mod)
        initList: list = list(vars(self.appContext))
        for attributeName in initList :
            if not attributeName.startswith("_"):
                print("init: "+attributeName)
                try:
                    mod = getattr(self.appContext,attributeName)
                    mod.init_plugin(self.appContext)
                except AttributeError as ex:
                    # warn has no init
                    print(ex)
                    print("Warning: cannot find init_plugin in plugin module " + file)
                except BaseException as ex:
                    # log exception
                    print(ex)




