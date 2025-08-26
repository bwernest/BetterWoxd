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

    def get_films_pages(self, user: str) -> list[BeautifulSoup]:
        print(f"Getting soup for user: {user}")
        page = 1
        valid_page = True
        pages_soup = []
        while valid_page:
            url = f"https://letterboxd.com/{user}/films/page/{page}"
            try:
                page_soup = self.get_soup(url)
                result = page_soup.find_all("div", class_="react-component")
                if len(result) == 1:
                    valid_page = False
                else:
                    pages_soup.append(page_soup)
                    page += 1
            except requests.RequestException:
                valid_page = False
        return pages_soup

    def get_soup(self, url: str) -> BeautifulSoup:
        print(f"Getting soup for URL: {url}")
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        return soup

    def get_films(self, user: str) -> list:
        pages_soup = self.get_films_pages(user)
        films = []
        for page_soup in pages_soup:
            for film in page_soup.find_all("div", class_="react-component"):
                title = film.get("data-item-full-display-name")
                films.append({"title": title})
        return films
