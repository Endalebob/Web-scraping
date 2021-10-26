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


def find_by_link(list_url):
    root = 'https://subslikescript.com/'
    response = requests.get(list_url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    box = soup.find('article', class_='main-article')
    for link in box.find_all('a', href=True):
        try:
            find_content(root + link['href'])
        except:
            pass

def find_pages():
    root = 'https://subslikescript.com/movies'
    response = requests.get(root)
    html_content = response.text
    soup = BeautifulSoup(html_content,'lxml')
    box = soup.find('ul','pagination')
    for page in box.find_all('a')[1:3]:
        print(page)
        find_by_link(root+'?page='+page.get_text())
        print(page.get_text())


find_pages()