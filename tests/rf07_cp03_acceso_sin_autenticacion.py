import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver


def test_rf07_cp03_acceso_sin_autenticacion():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("\n🔒 RF-07-CP03 – Acceso sin autenticación")

        driver.get("https://front-cine-gilt.vercel.app/my-tickets")

        # Redirección o bloqueo
        wait.until(
            EC.any_of(
                EC.url_contains("/login"),
                EC.title_contains("404")
            )
        )

        print("✅ Acceso restringido correctamente")
        print("✅ RESULTADO: Exitoso")

    finally:
        driver.quit()
