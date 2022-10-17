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
                self.RecursiveLoad(d)
        for attributeName in vars(self.appContext):
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
    def RecursiveLoad(self,path: str) :
        mod = importlib.import_module(path.replace("\\", "."))
        if hasattr(mod,"DEPENDENCIES") :
            dependencies: list = mod.DEPENDENCIES
            for dependency in dependencies :
                if not hasattr(self.appContext,dependency) :
                    dep_path:str = os.path.dirname(path)
                    self.RecursiveLoad(os.path.join(dep_path, dependency))
        self.appContext.addManager(os.path.basename(path), mod)

    def get_all_plugins(self) -> list:
        pluginList: list = list()
        for attributeName in vars(self.appContext):
            if not attributeName.startswith("_") :
                try:
                    mod = getattr(self.appContext,attributeName)
                    pluginList.append(mod)
                except BaseException as ex:
                    # log exception
                    print(ex)
        return pluginList




