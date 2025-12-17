import sys
import os
import time

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver
from utils.login import login

def test_rf03_cp02_cartelera_acceso_os():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🖥️ RF-03-CP02 – Acceso a cartelera con sistema operativo")
        print("📌 Objetivo: Verificar carga correcta de cartelera\n")

        login(driver)
        print("🔐 Login exitoso")

        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'grid')]")
            )
        )

        print("📄 Cartelera cargada correctamente")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
        print("🧹 Navegador cerrado\n")
