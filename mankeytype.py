from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    # Replace 'PATH_TO_CHROME_DRIVER' with the actual path to your Chrome WebDriver executable
    # Download Chrome WebDriver from: https://sites.google.com/a/chromium.org/chromedriver/downloads
    driver = webdriver.Chrome(executable_path='PATH_TO_CHROME_DRIVER')

    try:
        # Open the Monkeytype website
        driver.get('https://monkeytype.com/')

        # Wait for the website to load (you can adjust the sleep time if needed)
        time.sleep(5)

        # Keep the browser window open until the user closes it manually
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Script interrupted by the user.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
