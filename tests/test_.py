import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver", "open_login_page")
def test_ui_elements_start(driver):
    login_page = LoginPage(driver)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(login_page.logo_1))
    assert driver.find_element(*login_page.logo_1)
    assert driver.find_element(*login_page.logo_2)
    assert driver.find_element(*login_page.username_field)
    assert driver.find_element(*login_page.password_field)
    assert driver.find_element(*login_page.login_button)

@pytest.mark.usefixtures("driver", "open_login_page", "login")
def test_valid_login(driver):
    WebDriverWait(driver,10).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url.lower(), "Login failed!"

@pytest.mark.usefixtures("driver", "open_login_page", "login")
def test_goto_pim(driver):
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    dashboard_page = DashboardPage(driver)
    dashboard_page.go_to_pim()
    pim_page = PimPage(driver)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pim_page.employee_list_button))
    assert "pim" in driver.current_url.lower(), "PIM page was not opened!"
    assert driver.find_element(*pim_page.employee_list_button)
    assert driver.find_element(*pim_page.records)

@pytest.mark.usefixtures("driver", "open_login_page", "login")
def test_add_employee(driver):
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    dashboard_page = DashboardPage(driver)
    dashboard_page.go_to_pim()
    pim_page = PimPage(driver)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(pim_page.employee_list_button))
    pim_page = PimPage(driver)
    pim_page.add_new_employee()

    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(pim_page.personal_details)
    )
    assert success_message.is_displayed(), "Employee was not added successfully"

    pim_page.go_to_employee_list()

    pim_page.search_employee("Natalia")

    search_result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(pim_page.search)
    )
    assert "Natalia" in search_result.text, "Employee not found in the list"

# @pytest.mark.usefixtures("driver", "open_login_page", "login")
# def test_edit_employee(driver):


    # button = driver.find_element(By.XPATH, "//span[text()='Admin']")
    # button.click()
    #
    # time.sleep(3)


