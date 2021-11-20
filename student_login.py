
from home_page import *


def test_student_login(driver):
    open_home_page(driver)
    open_student_page(driver)
    student_login_form(driver)

    student_page_title = driver.find_element(By.CSS_SELECTOR, ".hidden-xs b")
    assert student_page_title.text == "rina@example.com"


def open_student_page(driver):
    student_module_locator = By.LINK_TEXT, "Student"
    student_module = driver.find_element(*student_module_locator)
    student_module.click()
    sleep(2)


def student_login_form(driver):
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.NAME, "submit")

    username.send_keys("rina@example.com")
    sleep(2)
    password.send_keys("admin@123")
    sleep(2)
    login_button.click()
    sleep(2)


























