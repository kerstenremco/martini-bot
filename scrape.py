# Run this script to scrape a webpage. Example: poetry run python3 scrape.py https://.....
from bs4 import BeautifulSoup
import requests
import sys

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
page = requests.get(sys.argv[1], headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
content = soup.find(class_='l-col--md-2-3')
title = content.find('h1').get_text().lower().replace(' ', '-')
text = content.find_all('p')
text_formatted = ""
for t in text:
    text_formatted += t.get_text()

with open(f"{title}.txt", "w") as file:
    file.write(text_formatted)