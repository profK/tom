from TomPluginManager import AppContext


class AccountManagerService():
    def __init__(self):
        print("Loaded ImageStoreService")

    def init_service(self, appContext: AppContext):
        global ctxt, imageDB
        ctxt = appContext
        accountDB = ctxt.Data.OpenTable("Accounts");

    def exposed_setHandle(self,handle:str):
        global accountDB
        xaction = accountDB.start_transaction()
        xaction.put(ctxt.username+".handle",handle)
        xaction.end()

    def expose_setImage(self, imagePath: str) :
        global accountDB
        xaction = accountDB.start_transaction()
        xaction.put(ctxt.username + ".image", imagePath)
        xaction.end()

    def exposed_getAccountInfo(self) :
        global accountDB
        xaction = accountDB.start_transaction()
        imagePath = xaction.get(ctxt.username + ".image")
        handle =  xaction.put(ctxt.username+".handle")
        xaction.end()
        return {
            "handle":handle,
            "imagePath": imagePath
        }
