"""___Modules_______________________________________________________________"""

from time import time
from ..toolbox import *

"""___Classes_______________________________________________________________"""

class Engine(Comparator, ToolBox):

    def set_users(self, users: list[str]) -> None:
        self.users = users

    def build_database(self):
        self.database = {}
        for user in self.users:
            self.database[user] = self.scrap(user)

    def build_stats(self):
        for user in self.users:
            self.database[user]["stats"] = self.get_individual_stats(self.database[user])
