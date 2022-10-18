# A singleton module
import importlib
import os
from types import ModuleType

global plugins


# holds plugins
class AppContext(object):
    def addManager(self, name: str, module: ModuleType):
        self.__setattr__(name, module)


class PluginManager:
    def __init__(self, ctxt: AppContext = None):
        if not ctxt == None:
            self.appContext = ctxt
        else:
            self.appContext = AppContext()

    def load_plugins(self, pluginDirectory: str = "plugins"):

        for file in os.listdir(pluginDirectory):
            d = os.path.join(pluginDirectory, file)
            if os.path.isdir(d):
                mod = importlib.import_module(d.replace("\\", "."))
                self.appContext.addManager(os.path.basename(d), mod)
        for attributeName in vars(self.appContext):
            if not attributeName.startswith("_"):
                print("init: " + attributeName)
                try:
                    mod = getattr(self.appContext, attributeName)
                    mod.init_plugin(self.appContext)
                except AttributeError as ex:
                    # warn has no init
                    print(ex)
                    print("Warning: cannot find init_plugin in plugin module " + file)
                except BaseException as ex:
                    # log exception
                    print(ex)

    def get_all_plugins(self) -> list:
        pluginList: list = list()
        for attributeName in vars(self.appContext):
            if not attributeName.startswith("_"):
                try:
                    mod = getattr(self.appContext, attributeName)
                    pluginList.append(mod)
                except BaseException as ex:
                    # log exception
                    print(ex)
        return pluginList




