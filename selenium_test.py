# selenium_test.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the Flask app URL
    driver.get("http://127.0.0.1:5000/")

    # Fill out the form
    driver.find_element(By.ID, 'username').send_keys('Test User')
    driver.find_element(By.ID, 'game_option').send_keys('Guess Game')
    driver.find_element(By.ID, 'difficulty').send_keys('3')

    # Submit the form
    driver.find_element(By.ID, 'difficulty').send_keys(Keys.RETURN)

    # Wait for results
    time.sleep(3)
    result_text = driver.find_element(By.TAG_NAME, 'p').text
    print(f"Test Result: {result_text}")

finally:
    driver.quit()
