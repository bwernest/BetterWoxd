"""___Modules_______________________________________________________________"""

# BetterWoxd
from betterwoxd.engine.engine import Engine

"""___Data__________________________________________________________________"""

users = [
    "bwernest",
]

"""___Execution_____________________________________________________________"""

engine = Engine(users)
engine.build_database()
for datum in engine.database["bwernest"]["films"]:
    print(datum)
