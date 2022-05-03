import requests
from bs4 import BeautifulSoup
url="https://yellowpages.com.tr/ara?q=B%C3%BCy%C3%BCk+Ma%C4%9Fazalar"
response=requests.get(url)

print(response)