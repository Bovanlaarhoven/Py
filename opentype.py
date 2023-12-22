import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def extract_letters(driver):
    words_container = driver.find_element(By.ID, 'words')
    words = words_container.find_elements(By.CLASS_NAME, 'word')

    result_text = ''
    for word in words:
        letters = [letter.text for letter in word.find_elements(By.TAG_NAME, 'letter')]
        result_text += ''.join(letters) + ' '

    return result_text.strip()

def simulate_typing(driver, text):
    textarea = driver.find_element(By.CLASS_NAME, 'mt-type-input')

    actions = ActionChains(driver)
    actions.move_to_element(textarea)

    for letter in text:
        actions.send_keys(letter)
        time.sleep(0.1)

    actions.perform()

def click_consent_button(driver):
    consent_button = driver.find_element(By.XPATH, '//button[@aria-label="Consent"]')
    consent_button.click()

website_url = 'https://monkeytype.com/'

driver = webdriver.Chrome()

try:
    driver.get(website_url)
    time.sleep(10)

    # Click the "Consent" button
    click_consent_button(driver)

    # Wait for the button click to take effect
    time.sleep(2)

    result_text = extract_letters(driver)
    print(result_text)

    simulate_typing(driver, result_text)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    driver.quit()
