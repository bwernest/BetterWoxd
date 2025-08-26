"""___Module________________________________________________________________"""

import requests
from lxml import html
from bs4 import BeautifulSoup

user = "bwernest"
page = 1

url = f"https://letterboxd.com/{user}/films/page/{page}/"

response = requests.get(url).text
# html_file = html.fromstring(response)
soup = BeautifulSoup(response, "html.parser")

def parse_films(soup):
    films = []
    for film in soup.find_all("div", class_="react-component"):
        title = film.get("data-item-full-display-name")
        films.append({"title": title})
    return films

print(parse_films(soup))
