import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = 'https://leetcode.com/accounts/login/'
option = Options()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)
driver.get(url)
username = 'aboambe'
password = 'Ru,/8R?Q!5g6iEM'
username_box = driver.find_element(By.XPATH, '//input[@id="id_login"]')
password_box = driver.find_element(By.XPATH, '//input[@id="id_password"]')
username_box.send_keys(username)
password_box.send_keys(password)
btn = driver.find_element(By.XPATH, '//button[@id="signin_btn"]')
btn.click()
contest_btn = driver.find_element(By.XPATH, '//a[@href="/contest/"]')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(contest_btn))
contest_btn.click()
contest_list = driver.find_elements(By.XPATH, '//div[@class="px-4"]')

for i in range(len(contest_list)):
    rank,name,score,time_finsh = [],[],[],[]
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable(contest_list[i]))
    contest_page = contest_list[i].find_element(By.XPATH, './/div/a')
    contest_page.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//a[@class="ranking-more-btn"]')))
    more_btn = driver.find_element(By.XPATH,'//a[@class="ranking-more-btn"]')
    more_btn.click()
    tr = driver.find_elements(By.XPATH,'//tr')
    contest_name = driver.find_element(By.XPATH,'//h1').text
    for i in range(1,len(tr)):
        trr = tr[i].find_elements(By.XPATH,'.//td')
        ele = trr[0].text
        rank.append(ele)
        ele = trr[1].text
        name.append(ele)
        ele = trr[2].text
        score.append(ele)
        ele = trr[3].text
        time_finsh.append(ele)
    driver.back()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/contest"]')))
    driver.back()
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="px-4"]')))
    contest_list = driver.find_elements(By.XPATH, '//div[@class="px-4"]')
    df = pd.DataFrame({"name":name,"rank":rank,"score":score,"finsh_time":time_finsh})
    print(df)
    df.to_csv(f"{contest_name}.csv",index=False)

driver.quit()
