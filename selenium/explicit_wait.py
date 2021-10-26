from selenium.webdriver.support import expected_conditions as EC
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

'''
syntax = WebDriverWait(driver,10).until(.2.)
2 = EC.presence_of_element_located(.3.)
By.XPATH,"value"
'''

# PATH = "C:/Users/Admin/Documents/chromedriver_win32/chromedriver.exe"
# ser = Service(PATH)
options = Options()
options.add_experimental_option("detach", True)
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

url = 'https://www.audible.co.uk/search?keywords=christian+books&ref-override=a_hp_t1_header_search&ref=nb_sb_ss_i_3_8&k=christian+books&crid=1E6WP6XX666ME&sprefix=christia%2Ceu-audible-uk%2C359&i=eu-audible-uk&url=search-alias%3Deu-audible-uk'
driver.get(url)
# driver.maximize_window()

target_content = driver.find_element(by=By.CLASS_NAME, value="adbl-impression-container ")
books = target_content.find_elements(by=By.XPATH, value='./div/span/ul/li')
title = []
author = []
length = []
list_page = driver.find_elements(By.XPATH,'//ul[contains(@class,"pagingElements")]/li')
n = int(list_page[-2].text)
for i in range(1,5):
    time.sleep(2)
    target_content = driver.find_element(by=By.CLASS_NAME, value="adbl-impression-container ")
    books = target_content.find_elements(by=By.XPATH, value='./div/span/ul/li')
    for book in books[:5]:
        try:
            title.append(book.find_element(by=By.XPATH, value='.//h3/a').text)
            author.append(book.find_element(by=By.XPATH, value='.//li[contains(@class,"authorLabel")]').text)
            length.append(book.find_element(by=By.XPATH, value='.//li[contains(@class,"runtimeLabel")]').text)
        except:
            print('nooo')
    if i != n:
        try:
            path = './/span[contains(@class," nextButton refinementFormButton")]/a'
            next_button = driver.find_element(By.XPATH,path)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable(next_button))
            driver.execute_script("arguments[0].click();", next_button)

        except:
            print(i)
driver.quit()
df = pd.DataFrame({"title": title, "author": author, "length": length})
df.to_csv('christian_audio_books.csv', index=False)
