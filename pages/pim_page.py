from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.employee_list_button = (By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and text()='Employee List']")
        self.records = (By.CSS_SELECTOR, "span.oxd-text.oxd-text--span")
        self.add = (By.XPATH, "//button[@type='button' and .//i[contains(@class, 'bi-plus')]]")
        self.first_name = (By.NAME, "firstName")
        self.last_name = (By.NAME, "lastName")
        self.save_btn = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--secondary.orangehrm-left-space")
        self.personal_details = (By.XPATH, "//h6[text()='Personal Details']")
        self.search = (By.XPATH, "//div[contains(text(), 'Natalia')]")
        self.emp_search_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_btn = (By.XPATH, "//button[@type='submit']")

    def open(self, url):
        self.driver.get(url)

    def add_new_employee(self):
        self.driver.find_element(*self.add).click()
        time.sleep(3)
        self.driver.find_element(*self.first_name).send_keys("Natalia")
        self.driver.find_element(*self.last_name).send_keys("New")
        time.sleep(3)
        self.driver.find_element(*self.save_btn).click()

    def go_to_employee_list(self):
        self.driver.find_element(*self.employee_list_button).click()

    def search_employee(self, first_name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.emp_search_name)).send_keys(
            first_name)
        self.driver.find_element(*self.search_btn).click()

