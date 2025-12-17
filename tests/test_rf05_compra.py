from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver

BASE_URL = "https://front-cine-gilt.vercel.app/"

def test_compra_entrada_exitosa():
    driver = get_driver()
    wait = WebDriverWait(driver, 40)

    driver.get(BASE_URL)

    # Login previo
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]"))).click()
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("selenium_test@mail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("12345678")
    driver.find_element(By.XPATH, "//button[contains(text(),'Ingres')]")).click()

    # Seleccionar primera película
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Ver')]"))).click()

    # Seleccionar función
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Función')]"))).click()

    # Seleccionar primer asiento disponible
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'seat')]"))).click()

    # Comprar
    driver.find_element(By.XPATH, "//button[contains(text(),'Comprar')]")).click()

    # Validar comprobante
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'PDF')]")))

    driver.quit()
