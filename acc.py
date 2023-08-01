import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# List of genders
genders = ['Female', 'Male']

# Randomly generate a username with 6 random letters
random_username = ''.join(random.choices(string.ascii_letters, k=6))

# Randomly generate a password with 8 characters (letters and digits)
random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Randomly select a gender
random_gender = random.choice(genders)

# Randomly select a birthday (day, month, and year)
random_day = random.randint(1, 28)
random_month = random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
random_year = random.randint(1990, 2003)  # Assuming users are between 18 and 33 years old

# Set up the Selenium WebDriver (Make sure you have the correct WebDriver for your browser installed)
driver = webdriver.Chrome()  # Change this to the path of your WebDriver if needed

driver.get("https://www.roblox.com/account/signupredir")

time.sleep(2.5)
try:
    dismiss_button = driver.find_element(By.CSS_SELECTOR, '.cookie-banner-btn.button-accept-all')
    dismiss_button.click()
except:
    pass

username_input = driver.find_element(By.ID, 'signup-username')
password_input = driver.find_element(By.ID, 'signup-password')
gender_buttons = driver.find_elements(By.CLASS_NAME, 'gender-button')

month_dropdown = Select(driver.find_element(By.ID, 'MonthDropdown'))
day_dropdown = Select(driver.find_element(By.ID, 'DayDropdown'))
year_dropdown = Select(driver.find_element(By.ID, 'YearDropdown'))

username_input.send_keys(random_username)
password_input.send_keys(random_password)

try:
    dismiss_button = driver.find_element(By.CSS_SELECTOR, '.cookie-banner-btn.button-accept-all')
    dismiss_button.click()
except:
    pass

for button in gender_buttons:
    if button.get_attribute('id').lower() == f"{random_gender.lower()}Button".lower():
        actions = ActionChains(driver)
        actions.move_to_element(button).click().perform()
        break

month_dropdown.select_by_value(random_month)
day_dropdown.select_by_value(str(random_day).zfill(2))
year_dropdown.select_by_value(str(random_year))

time.sleep(1)

signup_button = driver.find_element(By.ID, 'signup-button')
signup_button.click()

print(f"Username: {random_username}")
print(f"Password: {random_password}")

with open("generated_data.txt", "w") as file:
    file.write(f"Username: {random_username}\n")
    file.write(f"Password: {random_password}\n")

input("Press Enter to close the browser...")
driver.quit()
