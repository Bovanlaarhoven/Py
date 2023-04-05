import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Define a list of proxies
proxies = [
    '35.246.176.132:80',
    '213.247.38.132:80',
    '5.9.195.69:8080',
    '51.158.186.179:3128',
]

# Choose a random proxy from the list
proxy = random.choice(proxies)

# Set up the Chrome driver with the chosen proxy
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % proxy)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

# Define the list of URLs to randomly choose from
urls = [
    'https://link-hub.net/488828/key-hydra-network-best',
    'https://link-center.net/488828/key-for-hydra-network1',
]

# Choose a random URL from the list
url = random.choice(urls)

# Load the chosen URL with the driver and the proxy
driver.get(url)

# Wait for the page to load
time.sleep(10)

# Find the first button by class name and click it
button1 = driver.find_element(By.CLASS_NAME, "css-6dzqka")
button1.click()

# Wait for the page to load
time.sleep(10)

# Find the second button by class name and click it
button2 = driver.find_element(By.CLASS_NAME, "button-size.lv-darkgrey.lv-button-component.lv-button-size-desktop.lv-button-size-mobile.ng-star-inserted")
button2.click()

# Wait for the page to load
time.sleep(10)

# Find the third button by class name and click it
button3 = driver.find_element(By.CLASS_NAME, "buttonWrapper__button.lv-button-component.lv-button-size-desktop.lv-button-size-mobile.lv-orange")
button3.click()

# Wait for the page to load
time.sleep(10)

# Close the browser
driver.quit()
