from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

url = "https://letterboxd.com/bwernest"
page = requests.get(url)
soup = BeautifulSoup(html, "html.parser")
