from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim = (By.LINK_TEXT, "PIM")

    def open(self, url):
        self.driver.get(url)

    def go_to_pim(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.pim))
        self.driver.find_element(*self.pim).click()