from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import sys
import time
import os

def setup_driver():
   
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    
    chromedriver_path = ChromeDriverManager().install()
    chromedriver_binary = os.path.join(os.path.dirname(chromedriver_path), "chromedriver")
    
    
    driver = webdriver.Chrome(service=Service(chromedriver_binary), options=options)
    return driver

def test_wipe_scores_button(url):
   
    driver = setup_driver()
    driver.get(url)
    
    try:
       
        wipe_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/button")))
        wipe_button.click()
        
      
        time.sleep(1)
        
        
        score_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "score")))
        return "No scores available." in score_element.text
    except Exception as e:
        print(f"An error occurred during wipe scores test: {e}")
        return False
    finally:
        driver.quit()

def test_scores_service(url):
   
    driver = setup_driver()
    
    try:
        driver.get(url)
        
       
        score_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "score")))
        score_text = score_element.text
        return "User:" in score_text and "Game:" in score_text and "Difficulty" in score_text
    except Exception as e:
        print(f"An error occurred during scores service test: {e}")
        return False
    finally:
        driver.quit()

def main():
   
    url = "http://localhost:5000"
    
    if test_scores_service(url) and test_wipe_scores_button(url):
        print("Both tests passed.")
        sys.exit(0)
    else:
        print("One or more tests failed.")
        sys.exit(-1)

if __name__ == "__main__":
    main()
