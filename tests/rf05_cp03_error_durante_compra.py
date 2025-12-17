import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver
from utils.navigation import login, ir_a_horarios_interstellar, seleccionar_sala_imax


def test_rf05_cp03_error_durante_compra():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n❌ RF-05-CP03 – Error durante el proceso de compra")

        # Login y navegación normal
        login(driver, wait)
        ir_a_horarios_interstellar(driver, wait)
        seleccionar_sala_imax(driver, wait)

        # Intentar confirmar sin seleccionar asiento
        print("🛒 Intentando confirmar compra sin asientos")

        boton_confirmar = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[.//span[normalize-space()='Confirmar']]"
            ))
        )
        boton_confirmar.click()

        # Verificar mensaje de error visible
        mensaje_error = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//*[contains(text(),'error') or contains(text(),'selecciona')]"
            ))
        )

        print(f"⚠️ Mensaje mostrado: {mensaje_error.text}")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
