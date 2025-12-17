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

def test_rf02_cp03_login_campos_vacios():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n⚠️ RF-02-CP03 – Inicio de sesión con campos vacíos")
        print("📌 Objetivo: Verificar validación de campos obligatorios\n")

        driver.get(BASE_URL)
        print("➡️ Página de login cargada")
        time.sleep(1)

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Iniciar Sesión']")
            )
        ).click()
        print("🚀 Intento de login sin ingresar datos")
        time.sleep(1)

        assert "movies" not in driver.current_url
        print("⚠️ Validación correcta – Campos obligatorios requeridos")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
        print("🧹 Navegador cerrado correctamente\n")
