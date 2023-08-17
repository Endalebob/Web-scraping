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


def intern():
    worksheet = spreadsheet.get_worksheet(1)
    PATH = "C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    ser = Service(PATH)
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=ser)

    # Access website and scrape data
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

    df = pd.DataFrame({"Title": position, "Company": company, "Location": location, "Link": application_link,
                       "Date posted": date_posted})
    df = df[~df["Title"].str.split(" ").str[-1].str.contains('🇺🇸')]
    df = df[~df["Title"].str.split(" ").str[-1].str.contains('🛂')]
    # df = df.sort_index(ascending=False)
    existing_data = worksheet.get_all_values()

    # Keep the header row unchanged
    header_row = existing_data[0]

    # Prepare the new data without the header
    new_data = df.values.tolist()

    # Append the new data to the existing data, excluding the header
    updated_data = [header_row] + new_data

    # Clear the existing data in the worksheet
    worksheet.clear()

    # Update the worksheet with the updated data
    bunch = 100
    for i in range(0, len(updated_data), bunch):
        batch_rows = updated_data[i:i + bunch]
        worksheet.append_rows(batch_rows, value_input_option="RAW")

        print("Google Sheet updated!")


def new_grad():
    # Set up Selenium
    worksheet = spreadsheet.get_worksheet(1)
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
    df = df[~df["Title"].str.split(" ").str[-1].str.contains('🇺🇸')]
    # df = df.sort_index(ascending=False)
    # print(df)
    existing_data = worksheet.get_all_values()

    # Keep the header row unchanged
    header_row = existing_data[0]

    # Prepare the new data without the header
    new_data = df.values.tolist()

    # Append the new data to the existing data, excluding the header
    updated_data = [header_row] + new_data

    # Clear the existing data in the worksheet
    worksheet.clear()

    # Update the worksheet with the updated data
    bunch = 100
    for i in range(0, len(updated_data), bunch):
        batch_rows = updated_data[i:i + bunch]
        worksheet.append_rows(batch_rows, value_input_option="RAW")

    print("Google Sheet updated!")


while True:
    intern()
    new_grad()
    time.sleep(8 * 60 * 60)
