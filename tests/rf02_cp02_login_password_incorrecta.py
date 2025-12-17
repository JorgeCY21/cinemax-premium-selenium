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

def test_rf02_cp02_login_password_incorrecta():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n❌ RF-02-CP02 – Inicio de sesión con contraseña incorrecta")
        print("📌 Objetivo: Validar rechazo de credenciales\n")

        driver.get(BASE_URL)
        print("➡️ Página de login cargada")
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(
            "seleniumtest@gmail.com"
        )
        print("✍️ Correo electrónico ingresado")
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(
            "Incorrecta.1"
        )
        print("✍️ Contraseña incorrecta ingresada")
        time.sleep(1)

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Iniciar Sesión']")
            )
        ).click()
        print("🚀 Enviando credenciales incorrectas")
        time.sleep(2)

        assert "movies" not in driver.current_url
        print("⚠️ Acceso denegado – Credenciales inválidas")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
        print("🧹 Navegador cerrado correctamente\n")
