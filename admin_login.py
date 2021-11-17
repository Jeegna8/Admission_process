from driver_call import *


def test_admin_login(driver):
    # find student module
    admin_module = driver.find_element(By.LINK_TEXT, "Admin")
    admin_module.click()
    sleep(2)

    # on login page
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.NAME, "submit")

    username.send_keys("admin1@example.com")
    sleep(2)
    password.send_keys("admin345")
    sleep(2)
    login_button.click()
    sleep(2)

