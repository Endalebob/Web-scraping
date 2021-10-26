from bs4 import BeautifulSoup
import requests


def find_content(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    try:
        title = soup.find('h1').get_text()
        box = soup.find('article', class_='main-article')
        script = box.find('div', class_='full-script').get_text(separator=' ', strip=True)

        with open(f'{title}.txt', 'w', encoding="utf-8") as file:
            file.write(script)
    except:
        pass


def find_by_link():
    root = 'https://subslikescript.com/'
    list_url = 'https://subslikescript.com/movies'
    response = requests.get(list_url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    box = soup.find('article', class_='main-article')
    for link in box.find_all('a', href=True):
        try:
            find_content(root + link['href'])
        except:
            pass


find_by_link()
