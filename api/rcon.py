from mcrcon import MCRcon as r

class RconServer:
    def __init__(self, host: str, port: str, password: str):
        self.host = host
        self.port = int(port)
        self.password = password

    def getTPS(self):
        with r(self.host, self.password, port=self.port) as mcr:
            return mcr.command("tps")
            
    def getPlayers(self):
        with r(self.host, self.password, port=self.port) as mcr:
            return mcr.command("list")
        
    def op(self, target: str):
        with r(self.host, self.password, port=self.port) as mcr:
            mcr.command(f"op {target}")

    def deop(self, target: str):
        with r(self.host, self.password, port=self.port) as mcr:
            mcr.command(f"deop {target}")

    def serverReload(self):
        with r(self.host, self.password, port=self.port) as mcr:
            mcr.command("reload")

    def teleport(self, targets: str, location: str):
        with r(self.host, self.password, port=self.port) as mcr:
            mcr.command(f"tp {targets} {location}")
            
    def kick(self, target: str, reasone: str = None):
        with r(self.host, self.password, port=self.port) as mcr:
            if reasone is None:
                mcr.command(f"kick {target}")
            else:
                mcr.command(f"kick {target} {reasone}")

    def ban(self, target: str, reasone: str = None):
        with r(self.host, self.password, port=self.port) as mcr:
            if reasone is None:
                mcr.command(f"ban {target}")
            else:
                mcr.command(f"ban {target} {reasone}")

    def unban(self, target: str):
        with r(self.host, self.password, port=self.port) as mcr:
            mcr.command(f"pardon {target}")
 