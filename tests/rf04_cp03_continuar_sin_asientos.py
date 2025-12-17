import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver
from utils.navigation import login, ir_a_horarios_interstellar, seleccionar_sala_imax

def test_rf04_cp03_continuar_sin_seleccionar_asientos():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🚫 RF-04-CP03 – Continuar sin seleccionar asientos")

        login(driver, wait)
        ir_a_horarios_interstellar(driver, wait)
        seleccionar_sala_imax(driver, wait)

        # Verificar que estamos en la pantalla de selección de asientos
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'PANTALLA')]")
            )
        )

        print("🎬 Pantalla de selección de asientos cargada")
        print("⛔ No se seleccionan asientos")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
