from driver_call import *
from home_page import *

def test_admin_login(driver):
    open_home_page(driver)
    open_admin_page(driver)

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.NAME, "submit")

    username.send_keys("admin@example.com")
    sleep(2)
    password.send_keys("admin@123")
    sleep(2)
    login_button.click()
    sleep(2)

    admin_account_title = driver.find_element(By.CSS_SELECTOR, '.hidden-xs b')
    assert admin_account_title.text == "admin@example.com"

