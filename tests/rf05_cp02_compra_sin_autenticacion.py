import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver


def test_rf05_cp02_compra_sin_autenticacion():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🔒 RF-05-CP02 – Compra sin estar autenticado")

        # Intentar acceder directamente a movies
        driver.get("https://front-cine-gilt.vercel.app/movies")

        # El sistema debe redirigir al login
        wait.until(EC.url_contains("/login"))

        print("✅ Redirección automática a login")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
