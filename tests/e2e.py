from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys

def test_wipe_scores_button(url):
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    try:
        
        wipe_button = driver.find_element(By.XPATH, "/html/body/form/button")
        wipe_button.click()

        
        score_elements = driver.find_elements(By.CLASS_NAME, "score")
        if not score_elements:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()

def main():
    url = "http://localhost:5000"  
    if test_wipe_scores_button(url):
        print("Test passed.")
        sys.exit(0)
    else:
        print("Test failed.")
        sys.exit(-1)

if __name__ == "__main__":
    main()
