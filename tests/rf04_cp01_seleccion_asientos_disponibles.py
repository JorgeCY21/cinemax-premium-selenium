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

def test_rf04_cp01_seleccion_asientos_disponibles():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🎟️ RF-04-CP01 – Selección de asientos disponibles")

        login(driver, wait)
        ir_a_horarios_interstellar(driver, wait)
        seleccionar_sala_imax(driver, wait)

        print("🪑 Seleccionando asientos A-1 y A-2")

        asiento_a1 = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//span[normalize-space()='A-1']/parent::div"
            ))
        )
        asiento_a1.click()
        time.sleep(0.5)

        asiento_a2 = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//span[normalize-space()='A-2']/parent::div"
            ))
        )
        asiento_a2.click()
        time.sleep(0.5)

        print("✅ Asientos A-1 y A-2 seleccionados correctamente")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
