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

def test_rf03_cp01_cartelera_visible():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🎬 RF-03-CP01 – Visualización correcta de la cartelera")
        print("📌 Objetivo: Verificar que se muestren películas disponibles\n")

        login(driver)
        print("🔐 Login exitoso")

        titulo = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Películas en Cartelera')]")
            )
        )

        peliculas = driver.find_elements(By.XPATH, "//h3")

        assert titulo.is_displayed()
        assert len(peliculas) > 0

        print(f"🎞️ Películas encontradas: {len(peliculas)}")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
        print("🧹 Navegador cerrado\n")
