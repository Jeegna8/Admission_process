from driver_call import *
from home_page import *


def test_student_login(driver):
    open_home_page(driver)
    open_student_page(driver)

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.NAME, "submit")

    username.send_keys("rina@example.com")
    sleep(2)
    password.send_keys("admin@123")
    sleep(2)
    login_button.click()
    sleep(2)

    student_page_title = driver.find_element(By.CSS_SELECTOR, ".hidden-xs b")
    assert student_page_title.text == "rina@example.com"


















 #logout featur

    # user = driver.find_element(By.CLASS_NAME, "dropdown")
    # logout = driver.find_element(By.LINK_TEXT, "Logout")

    #user.click()
    #sleep(2)
    #logout.click()
    #sleep(2)











