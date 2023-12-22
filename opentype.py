import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pynput import keyboard

website_url = 'https://monkeytype.com/'
chrome_options = Options()
chrome_options.add_argument('--start-maximized') 
driver = webdriver.Chrome(options=chrome_options)
driver.get(website_url)

def on_activate():
    type_letters()

def extract_letters(driver):
    words_container = driver.find_element(By.ID, 'words')
    words = words_container.find_elements(By.CLASS_NAME, 'word')

    result_text = ''
    for word in words:
        letters = [letter.text for letter in word.find_elements(By.TAG_NAME, 'letter')]
        result_text += ''.join(letters) + ' '

    return result_text.strip()

def simulate_typing(driver, text):
    for letter in text:
        driver.switch_to.active_element.send_keys(letter)


def type_letters():
    try:

        result_text = extract_letters(driver)
        print(result_text)

        simulate_typing(driver, result_text)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        pass

with keyboard.GlobalHotKeys({'<ctrl>+<alt>': on_activate}) as h:
    h.join()