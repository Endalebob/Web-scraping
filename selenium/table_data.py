import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

PATH = "C:/Users/Admin/Documents/chromedriver_win32/chromedriver.exe"
ser = Service(PATH)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ser)


url = 'https://www.adamchoi.co.uk/overs/detailed'
driver.get(url)
all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
all_matches_button.click()

all_table = driver.find_elements('xpath','//tr')
data = []
home = []
score = []
far = []
for i in all_table:
    data.append(i.find_element('xpath','./td[1]').text)
    home.append(i.find_element('xpath','./td[2]').text)
    score.append(i.find_element('xpath','./td[3]').text)
    far.append(i.find_element('xpath','./td[4]').text)
driver.quit()
df = pd.DataFrame({'date':data,'home':home,'score':score,'far':far})
df.to_csv('match_statics.csv',index=False)
print(df)
