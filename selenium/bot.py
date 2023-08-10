import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = "C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
ser = Service(PATH)
options = Options()
options.add_experimental_option("detach", True)
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options, service=ser)

url = 'https://www.audible.co.uk/search?keywords=christian+books&ref-override=a_hp_t1_header_search&ref=nb_sb_ss_i_3_8&k=christian+books&crid=1E6WP6XX666ME&sprefix=christia%2Ceu-audible-uk%2C359&i=eu-audible-uk&url=search-alias%3Deu-audible-uk'
driver.get(url)
driver.maximize_window()

target_content = driver.find_element(by=By.CLASS_NAME, value="adbl-impression-container ")
books = target_content.find_elements(by=By.XPATH, value='./div/span/ul/li')
title = []
author = []
length = []
# time.sleep(5
for book in books:
    print(book)
    try:
        title.append(book.find_element(by=By.XPATH, value='.//h3/a').text)
        author.append(book.find_element(by=By.XPATH, value='.//li[contains(@class,"authorLabel")]').text)
        length.append(book.find_element(by=By.XPATH, value='.//li[contains(@class,"runtimeLabel")]').text)
    except:
        print('nooo')
driver.quit()
df = pd.DataFrame({"title": title, "author": author, "length": length})
print(df)
