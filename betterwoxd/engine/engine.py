"""___Modules_______________________________________________________________"""

from ..toolbox import *

"""___Classes_______________________________________________________________"""

class Engine(ToolBox):

    def __init__(self, users: list[str] = None) -> None:
        self.users = users if users is not None else []

    def build_database(self):
        self.database = {}
        for user in self.users:
            self.database[user] = self.scrap(user)
