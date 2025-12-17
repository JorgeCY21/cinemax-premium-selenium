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

def test_registro_usuario_valido():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🎬 INICIANDO PRUEBA RF-01: REGISTRO DE USUARIO VÁLIDO")

        driver.get(BASE_URL)
        print("➡️  Accediendo a CineMax")
        time.sleep(1)

        # 1. Click en Únete a CineMax
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Únete a CineMax']")
            )
        ).click()
        print("🖱️  Click en 'Únete a CineMax'")
        time.sleep(1)

        # 2. Llenado del formulario
        print("✍️  Ingresando nombres...")
        wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Juan")
        time.sleep(1)

        print("✍️  Ingresando apellidos...")
        driver.find_element(By.ID, "lastName").send_keys("Pérez")
        time.sleep(1)

        print("✉️  Ingresando correo electrónico (gmail)...")
        driver.find_element(By.ID, "email").send_keys("seleniumtest2@gmail.com")
        time.sleep(1)

        print("🔐 Ingresando contraseña válida...")
        driver.find_element(By.ID, "password").send_keys("Test.12")
        time.sleep(1)

        # 3. Click en Registrarse
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Registrarse']")
            )
        ).click()
        print("✅ Click en 'Registrarse'")
        time.sleep(1)

        # 4. Validación por URL final
        wait.until(EC.url_to_be(SUCCESS_URL))
        print("🎉 Registro exitoso – Redirección a /movies confirmada")

        print("✅ PRUEBA RF-01 FINALIZADA CON ÉXITO\n")

    finally:
        time.sleep(2)
        driver.quit()
        print("🧹 Navegador cerrado correctamente")
