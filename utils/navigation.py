from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://front-cine-gilt.vercel.app/"
SHOWTIMES_URL = "https://front-cine-gilt.vercel.app/showtimes/1"
SEATS_URL = "https://front-cine-gilt.vercel.app/seats/9"

def login(driver, wait):
    driver.get(BASE_URL)

    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(
        "seleniumtest@gmail.com"
    )
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(
        "Test.12"
    )

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Iniciar Sesión']")
        )
    ).click()

    wait.until(EC.url_contains("/movies"))

def ir_a_horarios_interstellar(driver, wait):
    btn_ver_horarios = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//h3[text()='Interstellar']/ancestor::div//button[contains(text(),'Ver Horarios')]"
        ))
    )
    btn_ver_horarios.click()

    wait.until(EC.url_to_be(SHOWTIMES_URL))

def seleccionar_sala_imax(driver, wait):
    sala = wait.until(
        EC.element_to_be_clickable((
            By.XPATH, "//h5[contains(text(),'Sala 1 - IMAX')]"
        ))
    )
    sala.click()

    wait.until(EC.url_to_be(SEATS_URL))
