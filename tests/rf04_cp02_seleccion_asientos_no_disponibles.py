import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver
from utils.navigation import login, ir_a_horarios_interstellar, seleccionar_sala_imax

def test_rf04_cp02_seleccion_asientos_no_disponibles():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🚫 RF-04-CP02 – Asientos no disponibles (A-1, A-2)")

        login(driver, wait)
        ir_a_horarios_interstellar(driver, wait)
        seleccionar_sala_imax(driver, wait)

        print("🔍 Verificando que los asientos A-1 y A-2 NO estén disponibles")

        asientos_a1 = driver.find_elements(
            By.XPATH,
            "//span[normalize-space()='A-1']/parent::div"
        )

        asientos_a2 = driver.find_elements(
            By.XPATH,
            "//span[normalize-space()='A-2']/parent::div"
        )

        assert len(asientos_a1) == 0
        assert len(asientos_a2) == 0

        print("✅ Asientos A-1 y A-2 no existen (ocupados correctamente)")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
