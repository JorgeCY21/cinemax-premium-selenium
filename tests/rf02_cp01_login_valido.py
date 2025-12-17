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
        print("📌 Objetivo: Verificar el acceso al sistema\n")

        driver.get(BASE_URL)
        print("➡️ Página de login cargada")
        time.sleep(1)

        # Email
        email_input = wait.until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email_input.clear()
        email_input.send_keys("seleniumtest@gmail.com")
        print("✍️ Correo electrónico ingresado")
        time.sleep(1)

        # Password
        password_input = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_input.clear()
        password_input.send_keys("Test.12")
        print("✍️ Contraseña ingresada")
        time.sleep(1)

        # Botón Iniciar Sesión
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Iniciar Sesión']")
            )
        ).click()
        print("🚀 Enviando credenciales")
        time.sleep(1)

        # Validación
        wait.until(EC.url_to_be(SUCCESS_URL))
        print("🎉 Acceso concedido – Redirección a /movies")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
        print("🧹 Navegador cerrado correctamente\n")
