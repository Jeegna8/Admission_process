from home_page import *


def open_student_page(driver):
    student_module_locator = By.LINK_TEXT, "Student"
    student_module = driver.find_element(*student_module_locator)
    student_module.click()
    sleep(2)


def student_login_form(driver, user_name, pass_word):
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.NAME, "submit")

    username.send_keys(user_name)
    sleep(2)
    password.send_keys(pass_word)
    sleep(2)
    login_button.click()
    sleep(2)


"""functions of sign up form"""
def open_sign_up_form(driver):
    sign_up_locator = By.LINK_TEXT, "Sign up now"
    sign_up = driver.find_element(*sign_up_locator)
    sign_up.click()
    sleep(2)


def signup_name(driver, stu_name):
    name_locator = By.NAME, "name"
    name = driver.find_element(*name_locator)
    name.send_keys(stu_name)
    sleep(2)


def signup_username(driver, u_name):
    username_locator = By.NAME, "username"
    username = driver.find_element(*username_locator)
    username.send_keys(u_name)
    sleep(2)


def signup_password(driver, passwrd):
    password_locator = By.NAME, "password"
    password = driver.find_element(*password_locator)
    password.send_keys(passwrd)
    sleep(2)


def signup_confirm_password(driver, confirm_passwrd):
    confirm_password_locator = By.NAME, "confirm_password"
    confirm_ = driver.find_element(*confirm_password_locator)
    confirm_.send_keys(confirm_passwrd)
    sleep(2)


def signup_submit(driver):
    submit_button_locator = By.XPATH, '//*[@id="form"]/div[5]/input'
    submit_button = driver.find_element(*submit_button_locator)
    submit_button.click()
    sleep(3)


def find_enquiry_form(driver):
    enquiry_form_locator = By.LINK_TEXT, "Enquiry Form"
    enquiry_form_open = driver.find_element(*enquiry_form_locator)
    enquiry_form_open.click()
    sleep(2)


"""functions for enquiry form"""
def enq_name(driver, student_name):
    name_locator = By.NAME, "fname"
    name = driver.find_element(*name_locator)
    name.send_keys(student_name)
    sleep(2)


def enq_email_id(driver, email_value):
    email_locator = By.NAME, 'email'
    email = driver.find_element(*email_locator).get_attribute("value")
    assert email == email_value


def enq_contact_no(driver, contact_num):
    contact_locator = By.NAME, "phone"
    contact = driver.find_element(*contact_locator)
    contact.send_keys(contact_num)
    sleep(2)


def enq_interested_field(driver, course_name):
    field_locator = By.NAME, 'courses'
    wait = WebDriverWait(driver, 10)
    subject_dropdown = wait.until(expected.element_to_be_clickable(field_locator))

    select = Select(subject_dropdown)
    select.select_by_visible_text(course_name)
    sleep(3)


def enq_register(driver):
    submit_btn_locator = By.TAG_NAME, "button"
    submit = driver.find_element(*submit_btn_locator)
    submit.click()
    sleep(3)


def enq_confirmation_message(driver):
    alert = Alert(driver)
    alert.accept()
    sleep(4)


def back_to_student_page(driver, username):
    student_page_title = driver.find_element(By.CSS_SELECTOR, ".hidden-xs b")
    assert student_page_title.text == username


"""student logout feature"""
def logout(driver):
    user_id_locator = By.CLASS_NAME, "dropdown"
    user_id = driver.find_element(*user_id_locator)
    user_id.click()

    log_out_locator = By.LINK_TEXT, "Logout"
    log_out = driver.find_element(*log_out_locator)
    log_out.click()
    sleep(3)


"""functions for query form"""
def find_query_form(driver):
    query_form_locator = By.LINK_TEXT, "Student Query"
    query_form = driver.find_element(*query_form_locator)
    query_form.click()


def que_email_id(driver, email_id):
    email_locator = By.NAME, 'email'
    email = driver.find_element(*email_locator).get_attribute("value")
    assert email == email_id
    sleep(2)


def type_query(driver, query):
    query_text_locator = By.NAME, "stu_query"
    query_text = driver.find_element(*query_text_locator)
    query_text.send_keys(query)
    sleep(3)


def send_query(driver):
    send_button_locator = By.TAG_NAME, "button"
    send_button = driver.find_element(*send_button_locator)
    send_button.click()
    sleep(2)

    assert driver.title == "Your Queries"
    sleep(5)

