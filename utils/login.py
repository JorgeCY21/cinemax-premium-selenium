import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://front-cine-gilt.vercel.app/"
SUCCESS_URL = "https://front-cine-gilt.vercel.app/movies"

def login(driver):
    wait = WebDriverWait(driver, 20)

    driver.get(BASE_URL)
    time.sleep(1)

    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(
        "seleniumtest@gmail.com"
    )
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(
        "Test.12"
    )

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Iniciar Sesión']")
        )
    ).click()

    wait.until(EC.url_to_be(SUCCESS_URL))
