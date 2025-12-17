import sys
import os
import time

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver

BASE_URL = "https://front-cine-gilt.vercel.app/"
SUCCESS_URL = "https://front-cine-gilt.vercel.app/movies"

def test_rf02_cp01_login_valido():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🔐 RF-02-CP01 – Inicio de sesión con credenciales válidas")

        driver.get(BASE_URL)
        time.sleep(1)

        # Ir a Login
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Iniciar sesión']")
        )).click()
        time.sleep(1)

        print("✉️ Ingresando correo válido")
        driver.find_element(By.ID, "email").send_keys("seleniumtest@gmail.com")
        time.sleep(1)

        print("🔑 Ingresando contraseña válida")
        driver.find_element(By.ID, "password").send_keys("Test.12")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[contains(text(),'Iniciar')]").click()
        time.sleep(1)

        wait.until(EC.url_to_be(SUCCESS_URL))
        print("✅ Acceso al sistema exitoso")

    finally:
        driver.quit()
