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

def test_rf01_cp03_registro_correo_existente():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n⚠️ RF-01-CP03 – Registro con correo ya registrado")

        driver.get(BASE_URL)
        time.sleep(1)

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Únete a CineMax']")
        )).click()
        time.sleep(1)

        driver.find_element(By.ID, "name").send_keys("Juan")
        time.sleep(1)

        driver.find_element(By.ID, "lastName").send_keys("Pérez")
        time.sleep(1)

        # Correo ya registrado
        driver.find_element(By.ID, "email").send_keys("seleniumtest@gmail.com")
        time.sleep(1)

        driver.find_element(By.ID, "password").send_keys("Test.12")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Registrarse']").click()
        time.sleep(2)

        # Validación: no redirige a /movies
        assert "movies" not in driver.current_url
        print("✅ Validación correcta – Correo duplicado rechazado")

    finally:
        driver.quit()
