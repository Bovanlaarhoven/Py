import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your chromedriver executable
webdriver_path = '/path/to/chromedriver'  # Replace with the actual path to your chromedriver

# URL to open in the browser
url = 'https://adfoc.us/8136161'  # Replace with the desired URL

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Uncomment this line if you want to run the browser in headless mode

# Create a new Chrome webdriver instance
driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

# Open the URL in the browser
driver.get(url)

# Wait for 5 seconds
time.sleep(5)

# Find the button by the image source
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[src="/images/serve/skip.png"]'))
)

# Click the button
button.click()

# Retrieve the page content
page_content = driver.page_source

# Close the browser window
driver.quit()
