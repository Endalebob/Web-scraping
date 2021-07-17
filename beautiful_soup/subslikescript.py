from bs4 import BeautifulSoup
import requests

url = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')
title = soup.find('h1').get_text()
script = soup.find('article', class_='main-article').find('div', class_='full-script').get_text(strip=True,
                                                                                                separator=' ')
# print(script)
with open(f'{title}.txt', 'w', encoding="utf-8") as file:
    file.write(script)
