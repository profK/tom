class TestProxy():
    def __init__(self):
        global ctxt

    def init_service(self,appContext):
        pass
    def exposed_ping(self):
        print("ping recieved at "+__file__)