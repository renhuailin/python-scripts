class StatusDict(dict):
    def __init__ (self):
        self["s"] = "fdsfsdfsd"


class ServerStatus :
    status = StatusDict()
    def __init__(self):
        pass


if __name__ == "__main__":
    ss = ServerStatus()
    print ss["s"]
