import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = "C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
ser = Service(PATH)
options = Options()
# options.add_experimental_option("detach", True)
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options, service=ser)

url = "https://github.com/SimplifyJobs/Summer2024-Internships"
driver.get(url)
driver.maximize_window()

target_content = driver.find_element(by=By.TAG_NAME, value="table")
target_content_body = target_content.find_elements(by=By.TAG_NAME, value="tbody")
target_content_rows = target_content_body[0].find_elements(by=By.TAG_NAME, value="tr")

company = []
position = []
location = []
application_link = []
date_posted = []
for row in target_content_rows:
    table_data = row.find_elements(by=By.TAG_NAME, value="td")
    if len(table_data) < 5:
        continue
    try:
        application_link.append(table_data[3].find_element(by=By.TAG_NAME, value="a").get_attribute("href"))
        company.append(table_data[0].text)
        position.append(table_data[1].text)
        location.append(table_data[2].text)
        date_posted.append(table_data[4].text)
    except:
        print("nooo")

driver.quit()

df = pd.DataFrame({"Title": position, "Company": company, "Location": location, "Link": application_link, "Date posted": date_posted})
print(df)
df = df[~df["Title"].str.split(" ").str[-1].str.contains('🇺🇸')]
df = df[~df["Title"].str.split(" ").str[-1].str.contains('🛂')]
df = df.sort_index(ascending=False)
df.to_csv("C:/Users/Admin/Downloads/Internship.csv", index=False)