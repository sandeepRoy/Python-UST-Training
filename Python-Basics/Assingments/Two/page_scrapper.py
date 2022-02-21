import requests
from bs4 import BeautifulSoup
import pickle

url = 'https://www.geeksforgeeks.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = set()
images = set()
for link in soup.find_all('a'):
    urls.add(link.get('href'))
for image in soup.find_all('img'):
    images.add(image.get('src'))

with open('scrapped_urls.txt', 'wb') as f:
    pickle.dump(urls, f)
with open('scrapped_images.txt', 'wb') as f:
    pickle.dump(urls, f)
