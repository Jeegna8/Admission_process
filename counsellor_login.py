from driver_call import *


def test_counsellor_login(driver):
    counsellor_module = driver.find_element(By.LINK_TEXT, "Councellor")
    counsellor_module.click()
    sleep(2)

    # on login page
    mail = driver.find_element(By.NAME, "mail")
    password = driver.find_element(By.NAME, "pass")
    login_button = driver.find_element(By.NAME, "btn")

    mail.send_keys("nikhil@couns2.com")
    sleep(2)
    password.send_keys("nikhil345")
    sleep(2)
    login_button.click()
    sleep(2)




