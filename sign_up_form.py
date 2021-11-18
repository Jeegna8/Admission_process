from driver_call import *
sign_up_locator = By.LINK_TEXT, "Sign up now"


def test_sign_up(driver):
    open_home_page(driver)
    open_student_page(driver)

    sign_up = driver.find_element(*sign_up_locator)
    sign_up.click()
    sleep(2)

    signup_page_title = driver.title
    assert signup_page_title == 'Sign Up'

    sign_up_form(driver)

    login_page_title = driver.title
    assert login_page_title == 'Login'  # we successfully signed up


def sign_up_form(driver):

    name_locator = By.NAME, "name"
    name = driver.find_element(*name_locator)

    username_locator = By.NAME, "username"
    username = driver.find_element(*username_locator)

    password_locator = By.NAME, "password"
    password = driver.find_element(*password_locator)

    confirm_password_locator = By.NAME, "confirm_password"
    confirm_password = driver.find_element(*confirm_password_locator)

    submit_button_locator = By.XPATH, '//*[@id="form"]/div[5]/input'
    submit_button = driver.find_element(*submit_button_locator)

    name.send_keys("Rina")
    sleep(2)
    username.send_keys("rina@example.com")
    sleep(2)
    password.send_keys("admin@123")
    sleep(2)
    confirm_password.send_keys("admin@123")
    sleep(2)
    submit_button.click()
    sleep(3)





