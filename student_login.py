from driver_call import *

def test_student_login(driver):

    # find student module
    student_module = driver.find_element(By.LINK_TEXT, "Student")
    student_module.click()
    sleep(2)

    # on login page
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.NAME, "submit")

    username.send_keys("nihar@email.com")
    sleep(2)
    password.send_keys("nihar345")
    sleep(2)
    login_button.click()
    sleep(2)

    enquiry_form=driver.find_element(By.LINK_TEXT, "Enquiry Form")
    enquiry_form.click()
    sleep(2)

    #form
    Name=driver.find_element(By.NAME, "fname")
    Name.send_keys("Nihar")
    sleep(2)

    Contact_no = driver.find_element(By.NAME, "phone")
    Contact_no.send_keys("7896541236")
    sleep(2)

    course_select=driver.find_element(By.NAME ,"courses")
    course_select.click()
    sleep(2)

    course_options = course_select.find_element_by_name(*By.NAME,"courses")
    for option in course_options:
        if option.text == "M.Tech" :
            option.click()


    #<span class="select2-selection__rendered" id="select2-courses-cv-container" title="BCA">BCA</span>

    #class ="select2-selection__rendered" id="select2-courses-cv-container" title="B.Tech UG" > B.Tech UG < / span >

    #subject_options_locator = (By.TAG_NAME, "option")
    #subject_options = subject_dropdown.find_elements(*subject_options_locator)
    #for option in subject_options:
     #   if option.text == "Webmaster":
      #      if not option.is_selected():
       #         option.click()

















 #logout featur

    # user = driver.find_element(By.CLASS_NAME, "dropdown")
    # logout = driver.find_element(By.LINK_TEXT, "Logout")

    #user.click()
    #sleep(2)
    #logout.click()
    #sleep(2)











