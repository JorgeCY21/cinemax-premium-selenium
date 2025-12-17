import sys
import os
import time

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.driver import get_driver
from utils.login import login

def test_rf03_cp03_cartelera_demora():
    driver = get_driver()
    wait = WebDriverWait(driver, 3)  # tiempo reducido

    try:
        print("\n⏳ RF-03-CP03 – Demora en la carga de cartelera")
        print("📌 Objetivo: Detectar carga tardía o parcial\n")

        login(driver)
        print("🔐 Login exitoso")

        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'grid')]")
            )
        )

        print("⚠️ Cartelera cargó dentro del tiempo")
        print("❌ RESULTADO: Fallido (no se evidenció demora)")

    except TimeoutException:
        print("🐌 La cartelera no cargó a tiempo")
        print("❌ RESULTADO: Fallido")

    finally:
        driver.quit()
        print("🧹 Navegador cerrado\n")
