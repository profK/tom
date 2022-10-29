class TestProxy():
    def __init__(self,appContext):
        global ctxt
        ctxt=appContext
        print(__class__)
    def exposed_ping(self):
        print("ping recieved at "+__file__)