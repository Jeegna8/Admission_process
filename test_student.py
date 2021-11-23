import pytest
from student_page import *
from admission_page import *
from upload_docs import *

@pytest.mark.signup
def test_sign_up(driver):
    open_home_page(driver)
    open_student_page(driver)
    open_sign_up_form(driver)

    signup_page_title = driver.title
    assert signup_page_title == 'Sign Up'

    signup_name(driver, fake.first_name())
    signup_username(driver, fake.email())
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
    pass_word = "admin@1234"
    student_login_form(driver, user_name, pass_word)

    student_page_title = driver.find_element(By.CSS_SELECTOR, ".hidden-xs b")
    assert student_page_title.text == user_name


@pytest.mark.login_fail
def test_login_fail(driver):
    open_home_page(driver)
    open_student_page(driver)

    user_name = "trisha@example.com"
    pass_word = "admin@123"
    student_login_form(driver, user_name, pass_word)

    errmsg = 'The password or username you entered was not valid.'
    assert login_error_msg(driver) == errmsg


@pytest.mark.forget_password
def test_forget_password(driver):
    open_home_page(driver)
    open_student_page(driver)

    find_forget_password(driver)
    reset_page(driver)
    forget_pass_username(driver, "trisha@example.com")
    forget_pass_new_password(driver, "admin@123")
    forget_pass_confirm_password(driver, "admin@123")
    forget_pass_submit(driver)

    assert driver.title == "Login"


@pytest.mark.inquiryform
def test_inquiry_form(driver):
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


@pytest.mark.query_form
def test_query_form(driver):
    test_student_login(driver)
    find_query_form(driver)

    email_id = "trisha@example.com"
    query = "I have query regarding courses."

    que_email_id(driver, email_id)
    type_query(driver, query)
    send_query(driver)


def test_display_query(driver):
    test_student_login(driver)

    my_queries_locator = By.XPATH, '//*[@id="side-menu"]/li[9]/a'
    my_queries = driver.find_element(*my_queries_locator)
    my_queries.click()
    sleep(4)

    query_display = driver.find_elements(By.XPATH, '//*[@id="st"]/tbody/tr[n]/td[1]')
    total_queries = len(query_display)
    print(total_queries)
    for query in query_display:
        print(query.text)


@pytest.mark.upload_documents
def test_upload_docs(driver):
    test_student_login(driver)
    find_upload_documents(driver)

    up_email(driver)
    upload_files(driver)
    uplod_button(driver)

    assert driver.title == 'View Documents'
    sleep(5)

    check_docs(driver)


@pytest.mark.view_docs
def test_view_docs(driver):
    test_student_login(driver)
    find_view_uploaded_docs(driver)

    check_docs(driver)














