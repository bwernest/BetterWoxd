"""___Modules_______________________________________________________________"""

from ..toolbox import *

"""___Classes_______________________________________________________________"""

class Engine(Comparator, ToolBox):

    def __init__(self, users: list[str] = None) -> None:
        self.users = users if users is not None else []

    def build_database(self):
        self.database = {}
        for user in self.users:
            self.database[user] = self.scrap(user)

    def build_stats(self):
        for user in self.users:
            self.database[user]["stats"] = self.get_individual_stats(self.database[user])
