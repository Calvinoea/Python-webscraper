import requests
from bs4 import BeautifulSoup
import urllib
import urllib.request
import urllib.parse

url = "https://webscraper.io/test-sites/e-commerce/allinone"


r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")


links = soup.find_all("a")

for link in links:
    link.get("href")


def unique_links(tags, url):
    cleaned_links = set()

    for link in links:
        link = link.get("href")

        if link is None:
            continue
        if link.endswith('/') or link.endswith('#'):
            link = link[-1]

        actual_url = urllib.parse.urljoin(url, link)
        cleaned_links.add(actual_url)

    return cleaned_links


cleaned_links = unique_links(links, url)


filename = "output_unique_weblink.csv"
f = open(filename, "w")
header = "Output_Weblinks\n"
f.write(header)


for link in cleaned_links:
    f.write(str(link) + '\n')
