from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open the Flask application
driver.get("http://127.0.0.1:5000/")

# Locate input fields and interact
name_field = driver.find_element(By.ID, 'username')
name_field.send_keys("Test User")

game_field = driver.find_element(By.ID, 'game_option')
game_field.send_keys("Game1")

# Submit the form
game_field.send_keys(Keys.RETURN)

# Wait and print the result
time.sleep(2)
print(driver.find_element(By.TAG_NAME, 'p').text)

# Close the driver
driver.quit()
 