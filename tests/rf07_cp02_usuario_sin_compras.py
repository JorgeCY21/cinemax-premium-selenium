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
MOVIES_URL = "https://front-cine-gilt.vercel.app/movies"


def test_rf07_cp02_usuario_sin_compras():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n📭 RF-07-CP02 – Usuario sin compras registradas")
        print("📌 Objetivo: Verificar mensaje informativo cuando no existen compras\n")

        # 1. Login
        driver.get(BASE_URL)
        print("➡️ Página de login cargada")
        time.sleep(1)

        # Email
        email_input = wait.until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email_input.clear()
        email_input.send_keys("ñarlitonuvzzz1@gmail.com")
        print("✍️ Correo electrónico ingresado")
        time.sleep(1)

        # Password
        password_input = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_input.clear()
        password_input.send_keys("Narlonuv1.11")
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

        # Validar acceso a movies
        wait.until(EC.url_to_be(MOVIES_URL))
        print("🎉 Login correcto – Redirección a /movies")

        # 2. Ir a "Mis entradas"
        boton_mis_entradas = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//a[contains(@href,'/my-tickets')]"
            ))
        )
        boton_mis_entradas.click()
        print("➡️ Acceso a Mis entradas")

        # 3. Validar mensaje exacto
        wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//*[normalize-space()='No tienes entradas aún']"
            ))
        )

        print("✅ Mensaje 'No tienes entradas aún' mostrado correctamente")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
        print("🧹 Navegador cerrado correctamente\n")
