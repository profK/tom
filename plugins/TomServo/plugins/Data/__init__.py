from typing import Any

from TomPluginManager import AppContext
import lmdb
import orjson
def init_plugin(ctxt:AppContext) :
    print("initted data")

env = lmdb.Environment("kv_store.lmdb",max_dbs=100)

class KVTable :
    def __init__(self,name:str) :
        self.db = env.open_db(name)

class Trans :
    def __init__(self,transaction:lmdb.Transaction):
        self.transaction = transaction
    def put(self,key:Any,value:Any) :
        self.transaction.put(orjson.dumps(key),orjson.dumps(value))
    def get(self,key) ->Any :
        b:bytes = self.transaction.get(orjson.dumps(key))
        if b==None :
            return None;
        return orjson.loads(b)
    def has(self,key:str) :
        return self.get(key) != None

    def end(self) :
        self.transaction.commit()

class KVTable :
    def __init__(self,name:str) :
        self.db = env.open_db(name.encode())
    def begin_transaction(self,write:bool=True) -> Trans:
        global env
        return Trans(env.begin(db=self.db,write=write,buffers=True))

def OpenTable(name:str) -> KVTable :
    return KVTable(name)
