from googlesearch import search
import requests
from bs4 import BeautifulSoup

query = input("Enter your query")

links = []
for link in search(query, tld="com", num=10, stop=10, pause=10):
    print(link)
    links.append(link)
try:
    url = requests.get(links[0])
    print(url.text)
except requests.exceptions.ConnectionError:
    print("No connection")
