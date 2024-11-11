from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys
import time

def test_wipe_scores_button(url):
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get(url)
    
    try:
       
        wipe_button = driver.find_element(By.XPATH, "/html/body/form/button")
        wipe_button.click()
        
        time.sleep(1)  
        
        score_element = driver.find_element(By.ID, "score")
        return "No scores available." in score_element.text

    except Exception as e:
        print(f"An error occurred during wipe scores test: {e}")
        return False

    finally:
        driver.quit()

def test_scores_service(url):
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)

       
        score_element = driver.find_element(By.ID, "score")
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
