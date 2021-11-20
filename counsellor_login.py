
from home_page import *


def test_counsellor_login(driver):
    open_home_page(driver)
    open_counsellor_page(driver)

    mail = driver.find_element(By.NAME, "mail")
    password = driver.find_element(By.NAME, "pass")
    login_button = driver.find_element(By.NAME, "btn")

    mail.send_keys("nilam@example.com")
    sleep(2)
    password.send_keys("admin@123")
    sleep(2)
    login_button.click()
    sleep(2)

    counsellor_account_title = driver.find_element(By.CSS_SELECTOR, 'li a .hidden-xs')
    assert counsellor_account_title.text == "Nilam Trivedi"


def open_counsellor_page(driver):
    counsellor_module_locator = By.LINK_TEXT, "Councellor"
    counsellor_module = driver.find_element(*counsellor_module_locator)
    counsellor_module.click()
    sleep(2)


