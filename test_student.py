import pytest
from student_page import *
from admission_page import *


@pytest.mark.signup
def test_sign_up(driver):
    open_home_page(driver)
    open_student_page(driver)
    open_sign_up_form(driver)

    signup_page_title = driver.title
    assert signup_page_title == 'Sign Up'

    signup_name(driver, "Trisha")
    signup_username(driver, "trisha@example.com")
    signup_password(driver, "admin@123")
    signup_confirm_password(driver, "admin@123")
    signup_submit(driver)

    login_page_title = driver.title
    assert login_page_title == 'Login'


@pytest.mark.login_pass
def test_student_login(driver):
    open_home_page(driver)
    open_student_page(driver)

    user_name = "trisha@example.com"
    pass_word = "admin@123"
    student_login_form(driver, user_name, pass_word)

    student_page_title = driver.find_element(By.CSS_SELECTOR, ".hidden-xs b")
    assert student_page_title.text == user_name

    logout(driver)


@pytest.mark.enquiryform
def test_enquiry_form(driver):
    test_student_login(driver)
    find_enquiry_form(driver)

    enq_name(driver, "Trisha")
    enq_email_id(driver, "trisha@example.com")
    enq_contact_no(driver, "9988776655")
    enq_interested_field(driver, "M.Tech")
    enq_register(driver)

    enq_confirmation_message(driver)
    back_to_student_page(driver, "trisha@example.com")   # check username ,if we are back to student dashboard


@pytest.mark.admission_form
def test_admission_form(driver):

    test_student_login(driver)
    find_admission_form(driver)

    ad_name(driver, "Trisha", "Nayak")
    ad_contact(driver, "9988776655")
    ad_email_id(driver, "trisha@example.com")
    gender(driver, "F")
    dob(driver, "23-05-1998")
    guardian_name(driver, "Hari")
    guardian_contact(driver, "9988776655")
    address(driver, "Rajkot")
    country(driver, "India")
    state(driver, "Gujarat")
    city(driver, "Rajkot")
    pincode(driver, "123456")
    degree_field(driver, "B.Arch")
    alert_message(driver)
    course(driver, "Research Architect")

    enroll_click(driver)
    confirmation_alert(driver)

    back_to_student_page(driver, "trisha@example.com")  # check username ,if we are back to student dashboard


