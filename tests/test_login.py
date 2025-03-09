import pytest
from pages.login_page import LoginPage
from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(config["DEFAULT"]["base_url"])
    login_page.login(config["login"]["username"], config["login"]["password"])

    assert "dashboard" in driver.current_url.lower(), "Login failed!"