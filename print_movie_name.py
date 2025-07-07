
import sys
from bs4 import BeautifulSoup
from tqdm import tqdm
import datetime
import requests
import os

dataset_location = os.path.realpath(os.path.join(os.path.dirname(__file__), "DataSets"))
current_year = int(datetime.datetime.now().year)
url = "https://www.imdb.com/search/title/?release_date=2024-01-01"
headers = {
    'User-Agent': 'My User Agent 1.0',
}
print(url)
response = requests.get(url, headers=headers)
text = response.text
# print(text)
soup = BeautifulSoup(text, "lxml")
# print(soup.find('title').text)
i = 1
movieList = soup.find_all('h3', attrs={'class':'ipc-title__text'})
for div_item in (movieList):
    print(div_item)