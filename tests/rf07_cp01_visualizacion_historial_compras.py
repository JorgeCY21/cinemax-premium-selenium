import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver
from utils.navigation import login


def test_rf07_cp01_visualizacion_historial_compras():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🎟️ RF-07-CP01 – Visualización del historial de compras")

        # Login
        login(driver, wait)

        # Asegurar estar en movies
        wait.until(EC.url_contains("/movies"))

        # Click en "Mis entradas"
        boton_mis_entradas = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//a[contains(@href,'/my-tickets') and contains(.,'Mis entradas')]"
            ))
        )
        boton_mis_entradas.click()

        # Verificar que aparece al menos una tarjeta de compra
        wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//div[contains(@class,'rounded-xl') and contains(@class,'border-gray-700')]"
            ))
        )

        print("✅ Historial de compras mostrado correctamente")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
