"""___Modules_______________________________________________________________"""

# BetterWoxd
from betterwoxd.engine.engine import Engine

"""___Execution______________________________________________________________"""

engine = Engine(users=["bwernest"])
url = "https://letterboxd.com/bwernest/films/page/9/"

soup = engine.get_soup(url)
result = soup.find_all("div", class_="react-component")
print(len(result))
