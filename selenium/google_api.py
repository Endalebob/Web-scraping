import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import gspread
from google.oauth2.service_account import Credentials
import time


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
# Google Sheets API setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "C:/Users/Admin/Downloads/for-api-395511-b7b23a63fa07.json"
SPREADSHEET_ID = "1aXh0OavV9f93Xs6aO0TEbFw2y0a4jrL3dgfYQXg92ns"

creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPE)
client = gspread.authorize(creds)
spreadsheet = client.open_by_key(SPREADSHEET_ID)
worksheet = spreadsheet.get_worksheet(4)
# Your existing code to fetch and process data using Selenium
# ...

driver.quit()
while True:
    # Fetch data using your code
    # ...

    df = pd.DataFrame({"Title": position, "Company": company, "Location": location, "Link": application_link, "Date posted": date_posted})

    # Update Google Sheet
    worksheet.clear()  # Clear existing data
    header = df.columns.tolist()
    worksheet.append_row(header)

    # Insert data rows
    for row in df.values.tolist():
        worksheet.append_row(row)

    print("Google Sheet updated!")

    time.sleep(12 * 60 * 60)

    time.sleep(12 * 60 * 60)  # Wait for 12 hours before updating again
