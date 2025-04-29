import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from configparser import ConfigParser

config = ConfigParser()
import os
print("Current working directory:", os.getcwd())
print("Config file exists:", os.path.exists("../config.ini"))
config.read(os.path.join(os.getcwd(), "../config.ini"))

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    print("WebDriver initialized")
    yield driver
    driver.quit()

@pytest.fixture
def open_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open(config["DEFAULT"]["base_url"])
    print(config["DEFAULT"]["base_url"])
    return login_page

@pytest.fixture
def login(open_login_page):
    open_login_page.login(config["login"]["username"], config["login"]["password"])


