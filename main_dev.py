"""___Modules_______________________________________________________________"""

# BetterWoxd
from betterwoxd.engine.engine import Engine

"""___Data__________________________________________________________________"""

users = [
    "bwernest",
    "zolkov",
    "JP78310",
]

"""___Execution_____________________________________________________________"""

engine = Engine(["zolkov"])
engine.build_database()
for datum in engine.database["zolkov"]["films"]:
    print(datum)
