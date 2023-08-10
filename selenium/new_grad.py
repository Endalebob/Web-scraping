import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import gspread
from google.oauth2.service_account import Credentials
import time

# Google Sheets API setup
SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]
CREDS_FILE = "C:/Users/Admin/Downloads/for-api-395511-b7b23a63fa07.json"
SPREADSHEET_ID = "1aXh0OavV9f93Xs6aO0TEbFw2y0a4jrL3dgfYQXg92ns"

creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPE)
client = gspread.authorize(creds)
spreadsheet = client.open_by_key(SPREADSHEET_ID)
worksheet = spreadsheet.get_worksheet(5)

while True:
    # Set up Selenium
    PATH = "C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    ser = Service(PATH)
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=ser)

    # Access website and scrape data
    url = "https://github.com/owini/New-Grad-Positions"
    driver.get(url)
    driver.maximize_window()

    target_content = driver.find_element(by=By.TAG_NAME, value="table")
    target_content_body = target_content.find_elements(by=By.TAG_NAME, value="tbody")
    target_content_rows = target_content_body[0].find_elements(by=By.TAG_NAME, value="tr")

    company = []
    position = []
    location = []
    application_link = []
    for row in target_content_rows:
        table_data = row.find_elements(by=By.TAG_NAME, value="td")
        if len(table_data) < 3:
            continue
        try:
            application_link.append(table_data[0].find_element(by=By.TAG_NAME, value="a").get_attribute("href"))
            company.append(table_data[0].text)
            position.append(table_data[2].text)
            location.append(table_data[1].text)
        except:
            print("nooo")

    driver.quit()

    df = pd.DataFrame({"Title": position, "Company": company, "Link": application_link, "Location": location})
    df = df.sort_index(ascending=False)
    print(df)
    worksheet.clear()

    # Batch update
    batch_data = [["Title", "Company", "Link", "Location"]]
    for i in range(len(df)):
        batch_data.append(df.iloc[i].to_list())
    worksheet.insert_rows(batch_data)
    print("Google Sheet updated!")

    # Sleep for 24 hours before the next update
    time.sleep(8 * 60 * 60)
