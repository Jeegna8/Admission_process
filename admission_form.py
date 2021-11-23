
from student_login import *


def test_enquiry_form(driver):

    test_student_login(driver)
    find_admission_form(driver)

    name(driver, "Rina", "Agrawal")
    contact(driver, "9988776655")
    email_id(driver, "rina@example.com")
    gender(driver, "F")
    dob(driver, "23-05-1998")
    guardian_name(driver, "keshav")
    guardian_contact(driver, "9988776655")
    address(driver, "Ahmedabad")
    country(driver, "India")
    state(driver, "Gujarat")
    city(driver, "Ahmedabad")
    pincode(driver, "123456")
    degree_field(driver, "B.Arch")
    alert_message(driver)
    course(driver, "Research Architect")

    enroll_click(driver)


def find_admission_form(driver):
    admission_form_locator = By.LINK_TEXT, "Admission Form"
    admission_form = driver.find_element(*admission_form_locator)
    admission_form.click()
    sleep(2)


def ad_name(driver, firstname, lastname):
    first_name_locator = By.NAME, "fname"
    last_name_locator = By.NAME, "lname"

    first_name = driver.find_element(*first_name_locator)
    first_name.send_keys(firstname)

    last_name = driver.find_element(*last_name_locator)
    last_name.send_keys(lastname)

    sleep(2)


def ad_contact(driver, contact_no):
    contact_locator = By.NAME, "contact"
    contact = driver.find_element(*contact_locator)
    contact.send_keys(contact_no)
    sleep(2)


def ad_email_id(driver, email_value):
    email_locator = By.NAME, 'mail'
    email = driver.find_element(*email_locator).get_attribute("value")
    assert email == email_value


def gender(driver, gen):
    male_select = driver.find_element(By.XPATH, "//input[@value='M']")
    female_select = driver.find_element(By.XPATH, "//input[@value='F']")

    if gen == "F":
        female_select.click()
    else:
        male_select.click()


def dob(driver, date):
    dob_locator = By.NAME, "dob"
    dob_ = driver.find_element(*dob_locator)
    dob_.send_keys(date)
    sleep(2)


def guardian_name(driver, g_name):
    guardian_locator = By.NAME, "gname"
    guardian = driver.find_element(*guardian_locator)
    guardian.send_keys(g_name)
    sleep(2)


def guardian_contact(driver, g_contact):
    guardian_contact_locator = By.NAME, "gcontact"
    guardian_cont = driver.find_element(*guardian_contact_locator)
    guardian_cont.send_keys(g_contact)
    sleep(2)


def address(driver, add):
    address_locator = By.NAME, "add"
    address_place = driver.find_element(*address_locator)
    address_place.send_keys(add)
    sleep(2)


def country(driver, con):
    country_locator = By.NAME, "country"
    country_place = driver.find_element(*country_locator)
    country_place.send_keys(con)
    sleep(2)


def state(driver, con):
    state_locator = By.NAME, "state"
    state_place = driver.find_element(*state_locator)
    state_place.send_keys(con)
    sleep(2)


def city(driver, city):
    city_locator = By.NAME, "city"
    city_place = driver.find_element(*city_locator)
    city_place.send_keys(city)
    sleep(2)


def pincode(driver, pin):
    pincode_locator = By.NAME, "pin"
    pin_ = driver.find_element(*pincode_locator)
    pin_.send_keys(pin)
    sleep(2)


def degree_field(driver, degree):
    field_locator = By.ID, "degree"
    wait = WebDriverWait(driver, 10)
    subject_dropdown = wait.until(expected.element_to_be_clickable(field_locator))

    select = Select(subject_dropdown)
    select.select_by_visible_text(degree)
    sleep(3)


def alert_message(driver):
    alert = driver.switch_to.alert
    #assert alert.text == f"You selected {degree}."
    alert.accept()
    sleep(2)


def course(driver, course_name):
    field_locator = By.NAME, "course"
    wait = WebDriverWait(driver, 10)
    subject_dropdown = wait.until(expected.element_to_be_clickable(field_locator))

    select = Select(subject_dropdown)
    select.select_by_visible_text(course_name)
    sleep(3)


def enroll_click(driver):
    submit_btn_locator = By.TAG_NAME, "button"
    submit = driver.find_element(*submit_btn_locator)
    submit.click()
    sleep(3)


def confirmation_alert(driver):
    alert = driver.switch_to.alert
    #assert alert.text == f"You selected {degree}."
    alert.accept()
    sleep(2)
