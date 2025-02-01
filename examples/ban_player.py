import os, time, requests
from iw4m import IW4MWrapper
from t6logreader import T6LogReader

class BanPlayerPlugin:
    def __init__(self):
        self.seen_commands = []

        self.iw4m = IW4MWrapper(
            base_url=os.environ['IW4M_URL'],
            server_id=os.environ['IW4M_ID'],
            cookie=os.environ['IW4M_HEADER']
        )

        self.server   = self.iw4m.Server(self.iw4m)
        self.commands = self.iw4m.Commands(self.iw4m)
        self.player   = self.iw4m.Player(self.iw4m) 

        self.log_reader = T6LogReader()

    def run(self):
        while True:
            last_line = self.log_reader.read_last_line()
            if last_line.startswith("]ban"):
                if last_line not in self.seen_commands:
                    self.commands.ban(last_line.split()[1], last_line.split()[2])
                    self.seen_commands.append(last_line)
            time.sleep(0.5)

plugin = BanPlayerPlugin()
plugin.run()
