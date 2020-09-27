#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/es/'

r = requests.get(url)

headers=BeautifulSoup(r.text,'html.parser').find_all('h2')

for header in headers:
    print(header.text)