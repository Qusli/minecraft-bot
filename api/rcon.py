from mcrcon import MCRcon as r

class RconServer:
    def __init__(self, host: str, port: str, password: str):
        self.host = host
        self.port = int(port)
        self.password = password

    def serverReload(self):
        with r(self.host, self.password, port=self.port) as mcr:
            mcr.command("reload")