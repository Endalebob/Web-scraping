import requests
from bs4 import BeautifulSoup

# Fetch the HTML content
url = 'https://www.example.com'
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Navigate the HTML tree and extract the data
title = soup.title.get_text()
links = [link['href'] for link in soup.find_all('a')]

# Store the data
print(title)
print(links)
