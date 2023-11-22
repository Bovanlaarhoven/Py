from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import random
import string
from random import choice
from faker import Faker


user_agent = UserAgent()
options = Options()
options.add_argument(f'user-agent={user_agent.random}')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-application-cache")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-offer-store-unmasked-wallet-cards")
options.add_argument("--disable-offer-upload-credit-cards")
options.add_argument("--disable-offer-upload-credit-cards")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-print-preview")
options.add_argument("--disable-prompt-on-repost")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-speech-api")
options.add_argument("--disable-sync")
options.add_argument("--disable-tab-for-desktop-share")
options.add_argument("--disable-translate")
options.add_argument("--disable-voice-input")
options.add_argument("--disable-wake-on-wifi")
options.add_argument("--enable-async-dns")
options.add_argument("--enable-simple-cache-backend")
options.add_argument("--enable-tcp-fast-open")
options.add_argument("--enable-webgl")
options.add_argument("--hide-scrollbars")
options.add_argument("--ignore-gpu-blacklist")
options.add_argument("--enable-logging")
options.add_argument("--log-level=0")
options.add_argument("--no-default-browser-check")
options.add_argument("--no-first-run")
options.add_argument("--no-managed-user-acknowledgment-check")
options.add_argument("--disable-web-security")
options.add_argument("--disable-xss-auditor")
driver = webdriver.Chrome(options=options)
website = "https://www.roblox.com"

def set_birthday():
    def select_random_option(dropdown_element):
        dropdown = Select(dropdown_element)
        options = [option.text for option in dropdown.options[1:]] 
        selected_option = random.choice(options)
        dropdown.select_by_visible_text(selected_option)
        print(f"Selected {selected_option}")

    day_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'DayDropdown'))
    )
    select_random_option(day_dropdown)

    month_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'MonthDropdown'))
    )
    select_random_option(month_dropdown)

    year_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'YearDropdown'))
    )
    select_random_option(year_dropdown)

def set_gender():
    gender_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.gender-button'))
    )

    random.shuffle(gender_buttons)
    random_gender_button = gender_buttons[0]
    driver.execute_script("arguments[0].scrollIntoView();", random_gender_button)
    random_gender_button.click()
    print(f"Selected gender: {random_gender_button.get_attribute('title')}")

def set_random_username():
    fake = Faker()
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'signup-username'))
    )

    random_username = ''.join(choice(string.ascii_letters + string.digits) for _ in range(8))

    username_input.clear()
    username_input.send_keys(random_username)
    print(f"Entered username: {random_username}")

def set_random_password():
    fake = Faker()
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'signup-password'))
    )
    random_password = fake.password(length=8)
    password_input.clear()
    password_input.send_keys(random_password)
    print(f"Entered password: {random_password}")

def click_sign_up_button():
    sign_up_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'signup-button'))
    )
    sign_up_button.click()
    print("Clicked the 'Sign Up' button")


def accept_cookie_banner():
    try:
        cookie_banner_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-cta-lg.cookie-btn.btn-primary-md.btn-min-width'))
        )
        cookie_banner_button.click()
        print("Accepted the cookie banner.")
    except:
        print("Cookie banner not found or already accepted.")


driver.get(website)

accept_cookie_banner()
time.sleep(1)
set_birthday()
time.sleep(1)
set_gender()
time.sleep(1)
set_random_username()
time.sleep(1)
set_random_password()
time.sleep(1)
click_sign_up_button()