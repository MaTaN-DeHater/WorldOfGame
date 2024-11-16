import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import pytest
import re


chromedriver_autoinstaller.install()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    try:
        driver = webdriver.Chrome(options=options)
        return driver
    except Exception as e:
        logger.error(f"Error setting up WebDriver: {e}")
        raise

@pytest.fixture
def url():

    return "http://127.0.0.1:8777"

def test_scores_service(url):

    driver = setup_driver()

    try:
        driver.get(url)


        score_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/pre"))
        )

        score_text = score_element.text.strip()
        logger.info(f"DEBUG: Found score text: {score_text}")


        score_match = re.search(r'Difficulty \d+: (\d+) Points', score_text)
        if score_match:
            score_value = int(score_match.group(1))
            logger.info(f"DEBUG: Parsed score value: {score_value}")
            assert 1 <= score_value <= 1000, f"Score is out of range: {score_value}"
        else:
            pytest.fail(f"Could not parse score from text: {score_text}")

    finally:
        driver.quit()

def test_wipe_scores_button(url):

    driver = setup_driver()

    try:
        driver.get(url)


        wipe_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/form/button"))
        )
        wipe_button.click()


        score_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/pre"))
        )

        score_text = score_element.text.strip()
        logger.info(f"DEBUG: Found score text after wiping: {score_text}")


        assert "No scores available." in score_text, "Scores are still present after wipe"

    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main()
