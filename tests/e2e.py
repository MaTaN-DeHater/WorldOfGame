from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

def test_wipe_scores_button(url):
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed and in your PATH
    driver.get(url)

    try:
        # Locate the "Wipe Scores" button using the provided XPath
        wipe_button = driver.find_element(By.XPATH, "/html/body/form/button")
        
        
        wipe_button.click()

        # Verify the action (e.g., check if scores are wiped)
        # This part depends on how your application behaves after wiping scores
        # For example, you might check if the score list is empty
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
