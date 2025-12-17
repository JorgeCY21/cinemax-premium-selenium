from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver

BASE_URL = "https://front-cine-gilt.vercel.app/"

def test_login_usuario_valido():
    driver = get_driver()
    wait = WebDriverWait(driver, 30)

    driver.get(BASE_URL)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]"))).click()

    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("selenium_test@mail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("12345678")

    driver.find_element(By.XPATH, "//button[contains(text(),'Ingres')]")).click()

    # Validar acceso a cartelera
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Cartelera')]")))

    driver.quit()
