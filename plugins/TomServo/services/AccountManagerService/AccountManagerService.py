from TomPluginManager import AppContext


class AccountManagerService():
    def __init__(self):
        print("Loaded ImageStoreService")

    def init_service(self, appContext: AppContext):
        global ctxt, imageDB
        ctxt = appContext
        accountDB = ctxt.Data.OpenTable("Accounts");

    def exposed_setAccountInfo(self,userInfo):
        global accountDB
        xaction = accountDB.start_transaction()
        xaction.put(ctxt.username+".info",userInfo)
        xaction.end()


    def exposed_getAccountInfo(self) :
        global accountDB
        xaction = accountDB.start_transaction()
        info = xaction.get(ctxt.username + ".info")
        xaction.end()
        return info
