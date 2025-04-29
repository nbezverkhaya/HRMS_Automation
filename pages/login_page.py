from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.logo_1 = (By.CSS_SELECTOR, 'img[src*="ohrm_branding.png"]')
        self.logo_2 = (By.CSS_SELECTOR, 'img[alt="orangehrm-logo"]')

    def open(self, url):
        print(f"Opening URL: {url}")
        self.driver.get(url)

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        )
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
