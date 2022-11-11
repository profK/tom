import inspect
import os
from typing import Any

from TomPluginManager import AppContext
import lmdb
import orjson

rootPath = os.path.dirname(inspect.getfile(inspect))

def init_plugin(ctxt:AppContext) :
    print("initted data")

env = lmdb.Environment(os.path.join(rootPath,"kv_store.lmdb"),max_dbs=100)


class Cursor :
    def __init__(self,cursor: lmdb.Cursor,prefix: str = None) :
        self.cursor = cursor
        if not prefix==None :
            while (not str(self.cursor.key()).startswith(prefix)) and (self.cursor.next()):
                pass # all work done in test

    def __iter__(self) :
        return self

    def __next__(self):
        if self.cursor.next() :
            return {"key": self.current_key(), "value": self.current_value()}
        else :
            raise StopIteration
    def current_key(self) :
        return self.cursor.key()

    def current_value(self) :
        return self.cursor.value()

    def next(self) :
        try :
            return self.__next__()
        except StopIteration :
            return None



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
    def cursor(self) :
        return Cursor(self.transaction.cursor())
    def end(self) :
        self.transaction.commit()


class KVTable:
    def __init__(self, name: str):
        self.db = env.open_db(name.encode())

    def begin_transaction(self, write: bool = True) -> Trans:
        global env
        return Trans(env.begin(db=self.db, write=write, buffers=True))

    def clearAll(self):
        with self.db.begin(write=True) as in_txn:
            in_txn.drop(self.db)

def OpenTable(name:str) -> KVTable :
    return KVTable(name)

