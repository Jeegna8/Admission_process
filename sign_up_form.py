from home_page import *
from student_login import open_student_page


def test_sign_up(driver):
    open_home_page(driver)
    open_student_page(driver)
    open_sign_up_form(driver)

    signup_page_title = driver.title
    assert signup_page_title == 'Sign Up'

    name(driver, "Rina")
    username(driver, "Rina@example.com")
    password(driver, "admin@123")
    confirm_password(driver, "admin@123")
    submit(driver)

    login_page_title = driver.title
    assert login_page_title == 'Login'  # we successfully signed up


def open_sign_up_form(driver):
    sign_up_locator = By.LINK_TEXT, "Sign up now"
    sign_up = driver.find_element(*sign_up_locator)
    sign_up.click()
    sleep(2)


def name(driver, stu_name):
    name_locator = By.NAME, "name"
    name = driver.find_element(*name_locator)
    name.send_keys(stu_name)
    sleep(2)


def username(driver, u_name):
    username_locator = By.NAME, "username"
    username = driver.find_element(*username_locator)
    username.send_keys(u_name)
    sleep(2)


def password(driver, passwrd):
    password_locator = By.NAME, "password"
    password = driver.find_element(*password_locator)
    password.send_keys(passwrd)
    sleep(2)


def confirm_password(driver, confirm_passwrd):
    confirm_password_locator = By.NAME, "confirm_password"
    confirm_ = driver.find_element(*confirm_password_locator)
    confirm_.send_keys(confirm_passwrd)
    sleep(2)


def submit(driver):
    submit_button_locator = By.XPATH, '//*[@id="form"]/div[5]/input'
    submit_button = driver.find_element(*submit_button_locator)
    submit_button.click()
    sleep(3)





