import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = "C:/Users/Admin/Documents/chromedriver_win32/chromedriver.exe"
ser = Service(PATH)
options = Options()
options.add_experimental_option("detach", True)
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options, service=ser)

url = ''
driver.get(url)
driver.maximize_window()

# wait of 6 seconds to let the page load the content
time.sleep(6)  # this time might vary depending on your computer

# locating username and password inputs and sending text to the inputs
# username
username = driver.find_element(By.XPATH,'//input[@autocomplete ="username"]')
username.send_keys("my_username")  # Write Email Here
# username.send_keys(os.environ.get("TWITTER_USER"))

# Clicking on "Next" button
next_button = driver.find_element(By.XPATH,'//div[@role="button"]//span[text()="Next"]')
next_button.click()

# wait of 2 seconds after clicking button
time.sleep(2)

# password
password = driver.find_element(By.XPATH,'//input[@autocomplete ="current-password"]')
password.send_keys("my_password")  # Write Password Here
# password.send_keys(os.environ.get("TWITTER_PASS"))

# locating login button and then clicking on it
login_button = driver.find_element(By.XPATH,'//div[@role="button"]//span[text()="Log in"]')
login_button.click()

# closing driver
# driver.quit()
