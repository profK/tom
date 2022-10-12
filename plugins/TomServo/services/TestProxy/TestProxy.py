class TestProxy():
    def __init__(self):
        print(__class__)
    def exposed_ping(self):
        print("ping recieved at "+__file__)