import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Initialize the Chrome driver
url = 'https://www.fiverr.com/hammad_rauf/scrape-website-within-24-hour?context_referrer=logged_in_homepage&source=by_recently_viewed&ref_ctx_id=23abe9617b4879b2abd382efda496e57&context=recommendation&pckg_id=1&pos=1&context_alg=recently_viewed&seller_online=true&imp_id=ab991183-dcfc-4c32-a6e8-cfd396a3a6ea'
option = Options()
option.add_experimental_option("useAutomationExtension", False)
print('hello')
option.add_argument("user-agent=whatever you want")
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)
driver.get(url)  # Replace with the URL of the website you want to scrape
print('hello')

# Find the "See More" button
see_more_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"reviews-wrap")]/div[contains(@class,"load-more-wrapper")]/button')))
# Replace 'XPATH_OF_THE_SEE_MORE_BUTTON' with the actual XPath of the "See More" button on the website

# Loop to click the "See More" button until it disappears
while True:
    try:
        # Click the "See More" button
        see_more_button.click()
        WebDriverWait(driver, 20).until(EC.staleness_of(see_more_button))  # Wait for the button to become stale
        time.sleep(5)  # Add a delay to allow the new reviews to load
    except:
        # If the "See More" button is not found or is not clickable, break the loop
        break

# Extract the reviews
reviews = driver.find_elements(By.XPATH, '//div[contains(@class,"reviews-wrap")]/ul/span/li/div[contains(@class,"review-details")]/div[contains(@class,"review-description")]/p')
# Replace 'XPATH_OF_THE_REVIEWS' with the actual XPath of the reviews on the website

# Loop through the reviews and print or store them as needed
print(reviews)
value = []
for review in reviews:
    m = review.get_attribute('textContent')  # Use get_attribute('textContent') to extract the text from the p element
    value.append(m)

# Close the Chrome driver
print(value)
driver.quit()
