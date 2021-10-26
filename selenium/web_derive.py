'''
    before:

    from selenium import webdriver
    chrome_driver_path = 'C:/Users/Morteza/Documents/Dev/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    url = "https://www.google.com"
    driver.get(url)
    after:

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    s=Service('C:/Users/Morteza/Documents/Dev/chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    url='https://www.google.com'
    browser.get(url)
'''

# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# url = 'https://www.adamchoi.co.uk/overs/detailed'
# driver.get(url)
# all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
# all_matches_button.click()

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
