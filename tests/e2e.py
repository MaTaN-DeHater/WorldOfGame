import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

chromedriver_autoinstaller.install()


def setup_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    return driver


def test_scores_service(url):

    driver = setup_driver()

    try:
        driver.get(url)


        score_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/pre"))
        )


        score_text = score_element.text.strip()
        print(f"DEBUG: Found score text: {score_text}")

        try:
            score_value = int(score_text.split()[-1])
            print(f"DEBUG: Parsed score value: {score_value}")
            if 1 <= score_value <= 1000:
                print("test_scores_service: Passed")
                return True
            else:
                print("test_scores_service: Failed - Score out of range")
                return False

        except ValueError:
            print(f"test_scores_service: Failed - Could not parse score from text: {score_text}")
            return False

    except Exception as e:
        print(f"test_scores_service: Failed with error: {e}")
        return False

    finally:
        driver.quit()


def test_wipe_scores_button(url):

    driver = setup_driver()
    driver.get(url)

    try:

        wipe_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/form"))
        )
        wipe_button.click()


        score_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/pre"))
        )

        if "No scores available." in score_element.text:
            print("test_wipe_scores_button: Passed")
            return True
        else:
            print("test_wipe_scores_button: Failed - Scores are still present")
            return False

    except Exception as e:
        print(f"test_wipe_scores_button: Failed with error: {e}")
        return False

    finally:
        driver.quit()


def main():

    url = "http://127.0.0.1:8777/score"

    scores_service_passed = test_scores_service(url)
    wipe_scores_passed = test_wipe_scores_button(url)

    if scores_service_passed and wipe_scores_passed:
        print("Both tests passed.")
        sys.exit(0)
    else:
        print("One or more tests failed.")
        sys.exit(-1)


if __name__ == "__main__":
    main()
