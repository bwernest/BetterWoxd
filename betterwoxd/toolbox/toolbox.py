"""___Modules_______________________________________________________________"""

# BetterWoxd
from .settings import Settings

# Python
import requests
from bs4 import BeautifulSoup

"""___Classes_______________________________________________________________"""

class ToolBox(Settings):
    
    def scrap(self, user: str) -> dict:
        print(f"Scraping data for user: {user}")
        data = {
            "user": user,
            "films": self.get_films(user)
        }
        return data

    def get_soup(self, user: str) -> BeautifulSoup:
        print(f"Getting soup for user: {user}")
        page = 1
        is_page = True
        while is_page:
            url = f"https://letterboxd.com/{user}/films/page/{page}"
            try:
                print(f"Page: {page}")
                response = requests.get(url).text
                soup = BeautifulSoup(response, "html.parser")
                page += 1
            except requests.RequestException:
                is_page = False
        return soup

    def get_films(self, soup: BeautifulSoup) -> list:
        films = []
        for film in soup.find_all("div", class_="react-component"):
            title = film.get("data-item-full-display-name")
            films.append({"title": title})
        return films
