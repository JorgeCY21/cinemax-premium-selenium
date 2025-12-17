import sys
import os
import time

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver
from utils.navigation import login, ir_a_horarios_interstellar, seleccionar_sala_imax


def test_rf05_cp01_compra_entradas_exitosa():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🎟️ RF-05-CP01 – Compra de entradas exitosa")

        # 1. Login y navegación
        login(driver, wait)
        ir_a_horarios_interstellar(driver, wait)
        seleccionar_sala_imax(driver, wait)

        # 2. Seleccionar asiento A-3
        print("🪑 Seleccionando asiento A-3")

        asiento_a3 = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//span[normalize-space()='A-3']/parent::div"
            ))
        )
        asiento_a3.click()
        time.sleep(0.5)

        # 3. Confirmar selección de asiento
        print("🛒 Confirmando selección")

        boton_confirmar = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[.//span[normalize-space()='Confirmar']]"
            ))
        )
        boton_confirmar.click()

        # 4. Redirección automática a confirmation
        wait.until(EC.url_contains("/confirmation"))
        print("✅ En pantalla de confirmation")

        # 5. Confirmar y pagar
        print("💳 Confirmando y pagando ahora")

        boton_pagar = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[normalize-space()='Confirmar y Pagar Ahora']"
            ))
        )
        boton_pagar.click()

        # 6. Retorno final a movies
        wait.until(EC.url_contains("/movies"))
        print("✅ Retorno final a cartelera (movies)")

        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
