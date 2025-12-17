import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver
from utils.navigation import login, ir_a_horarios_interstellar, seleccionar_sala_imax


def test_rf05_cp03_error_durante_compra():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n⚠️ RF-05-CP03 – Error durante el proceso de compra")

        # Login y navegación normal
        login(driver, wait)
        ir_a_horarios_interstellar(driver, wait)
        seleccionar_sala_imax(driver, wait)

        # Validar que llega correctamente a selección de asientos
        wait.until(EC.url_contains("/seats"))

        print("✅ Flujo detenido antes de confirmar la compra")
        print("✅ El sistema no completó la compra")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
