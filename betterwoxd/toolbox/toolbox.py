"""___Modules_______________________________________________________________"""

# BetterWoxd
from .settings import Settings

# Python
from bs4 import BeautifulSoup
import requests
import time

"""___Classes_______________________________________________________________"""

class ToolBox(Settings):
    
    def scrap(self, user: str) -> dict:
        print(f"Scraping data for user: {user}")
        metadata = self.get_metadata(user)
        data = {
            "user": user,
            "films": self.get_films(user)
        }
        return data

    def get_metadata(self, user: str) -> dict:
        page_soup = self.get_home_page(user)
        metadata = {}
        print("QUOICOUBEH")
        print(page_soup.find("h4", class_="profile-statistic statistic").text)
        # metadata["username"] = page_soup.find("h4", class_="profile-statistic statistic").text.strip()[:-5]
        metadata["films_count"] = int((page_soup.find("h4", class_="profile-statistic statistic").text).strip()[:-5])
        # metadata["lists"] = int(page_soup.find("span", class_="statistic-value").text.strip())
        # metadata["following_count"] = int(page_soup.find("span", class_="statistic-value").text.strip())
        # metadata["followers_count"] = int(page_soup.find("span", class_="statistic-value").text.strip())
        self.export_soup(page_soup)
        print(metadata)
        return metadata

    def export_soup(self, soup: BeautifulSoup) -> None:
        timestamp = int(time.time())
        file_name = f"{self.export_path}/exported_soup_{timestamp}.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"Soup exported to {file_name}")

    def get_home_page(self, user: str) -> BeautifulSoup:
        print(f"Getting home page for user: {user}")
        if self.test:
            file_name = f"{self.data_path}/{user}_home_page.html"
            print(f"Getting offline soup for URL: {file_name}")
            with open(file_name, "r", encoding="utf-8") as f:
                response = f.read()
        else:
            url = f"https://letterboxd.com/{user}/"
            response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        return soup

    def get_films_pages(self, user: str) -> list[BeautifulSoup]:
        print(f"Getting soup for user: {user}")
        page = 1
        valid_page = True
        pages_soup = []
        while valid_page:
            url_info = {"user": user, "page": page}
            try:
                page_soup = self.get_soup(url_info)
                result = page_soup.find_all("div", class_="react-component")
                if len(result) < 2:
                    valid_page = False
                else:
                    pages_soup.append(page_soup)
                    page += 1
            except requests.RequestException:
                valid_page = False
            time.sleep(3*(not self.test))
        return pages_soup

    def get_soup(self, url_info: dict) -> BeautifulSoup:
        if self.test:
            return self.get_offline_soup(url_info)
        else:
            return self.get_online_soup(url_info)

    def get_online_soup(self, url_info: dict) -> BeautifulSoup:
        url = f"https://letterboxd.com/{url_info['user']}/films/page/{url_info['page']}/"
        print(f"Getting soup for URL: {url}")
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        return soup

    def get_offline_soup(self, url_info: dict) -> BeautifulSoup:
        print(f"Getting offline soup for URL: {url_info}")
        file_name = f"{self.data_path}/{url_info['user']}_films_page_{url_info['page']}.html"
        with open(file_name, "r", encoding="utf-8") as f:
            print(f"Reading file: {file_name}")
            response = f.read()
        soup = BeautifulSoup(response, "html.parser")
        return soup

    def get_films(self, user: str) -> list:
        pages_soup = self.get_films_pages(user)
        films = []
        for page_soup in pages_soup:
            for film in page_soup.find_all("div", class_="react-component"):
                raw_title = film.get("data-item-full-display-name")
                if raw_title is not None:
                    title, year = self.split_title(raw_title)
                    films.append({"title": title, "year": year})
        return films

    def split_title(self, raw_title: str) -> tuple[str, int]:
        title, year = raw_title.rsplit(" (", 1)
        year = int(year[:-1])  # Remove the closing parenthesis and convert to int
        return title, year
