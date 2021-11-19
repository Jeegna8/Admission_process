from driver_call import *
from student_login import *


def test_enquiry_form(driver):

    test_student_login(driver)
    find_enquiry_form(driver)

    name(driver, "Rina")
    email_id(driver, "rina@example.com")
    contact_no(driver, "9988776655")
    interested_field(driver, "BCA")
    register(driver)
    
    confirmation_message(driver)
    back_to_student_page(driver)


def find_enquiry_form(driver):
    enquiry_form_locator = By.LINK_TEXT, "Enquiry Form"
    enquiry_form_open = driver.find_element(*enquiry_form_locator)
    enquiry_form_open.click()
    sleep(2)


def name(driver, student_name):
    name_locator = By.NAME, "fname"
    name = driver.find_element(*name_locator)
    name.send_keys(student_name)
    sleep(2)


def email_id(driver, email_value):
    email_locator = By.NAME, 'email'
    email = driver.find_element(*email_locator).get_attribute("value")
    assert email == email_value


def contact_no(driver, contact_num):
    contact_locator = By.NAME, "phone"
    contact = driver.find_element(*contact_locator)
    contact.send_keys(contact_num)
    sleep(2)


def interested_field(driver, course_name):
    field_locator = By.NAME, 'courses'
    wait = WebDriverWait(driver, 10)
    subject_dropdown = wait.until(expected.element_to_be_clickable(field_locator))

    select = Select(subject_dropdown)
    select.select_by_visible_text(course_name)
    sleep(3)


def register(driver):
    submit_btn_locator = By.TAG_NAME, "button"
    submit = driver.find_element(*submit_btn_locator)
    submit.click()
    sleep(3)


def confirmation_message(driver):
    alert = Alert(driver)
    alert.accept()
    sleep(4)


def back_to_student_page(driver):
    student_page_title = driver.find_element(By.CSS_SELECTOR, ".hidden-xs b")
    assert student_page_title.text == "rina@example.com"







