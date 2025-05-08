from mcrcon import MCRcon as r

class RconServer:
    def __init__(self, host: str, port: str, password: str):
        self.host = host
        self.port = int(port)
        self.password = password

    def serverReload(self):
        with r(self.host, self.password, port=self.port) as mcr:
            mcr.command("reload")

    def teleport(self, targets: str, location: str = None):
        with r(self.host, self.password, port=self.port) as mcr:
            if location is None:
                mcr.command(f"tp {targets}")
            else:
                mcr.command(f"tp {targets} {location}")