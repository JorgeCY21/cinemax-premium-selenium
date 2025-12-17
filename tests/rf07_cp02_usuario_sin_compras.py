import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver
from utils.navigation import login


def test_rf07_cp02_usuario_sin_compras():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n📭 RF-07-CP02 – Usuario sin compras registradas")

        # Login (usuario sin compras)
        login(driver, wait)

        wait.until(EC.url_contains("/movies"))

        # Ir a Mis entradas
        driver.find_element(By.XPATH, "//a[contains(@href,'/my-tickets')]").click()

        # Validar mensaje informativo
        wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//*[contains(text(),'no') and contains(text(),'entradas')]"
            ))
        )

        print("✅ Mensaje informativo mostrado correctamente")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
