from home_page import *


def find_upload_documents(driver):
    upload_docs_locator = By.LINK_TEXT, "Upload Documents"
    upload_docs = driver.find_element(*upload_docs_locator)
    upload_docs.click()


def up_email(driver):
    email_locator = By.ID, 'fname'
    email = driver.find_element(*email_locator).get_attribute("value")
    assert email == "trisha@example.com"
    sleep(3)


def upload_files(driver):

    img_10th_locator = By.XPATH, '//*[@type="file"]'
    img_12th_locator = By.ID, 'img2'
    img_LC_locator = By.ID, 'img3'
    img_aadhar_locator = By.ID, 'img4'

    marksheet_path = os.path.abspath('C:/Users/K.B.P/Desktop/Automation/marksheet.png')
    lc_path = os.path.abspath('C:/Users/K.B.P/Desktop/Automation/LC.png')
    aadhar_path = os.path.abspath('C:/Users/K.B.P/Desktop/Automation/aadhar.png')

    doc_10th = driver.find_element(*img_10th_locator)
    doc_12th = driver.find_element(*img_12th_locator)
    doc_LC = driver.find_element(*img_LC_locator)
    doc_aadhar = driver.find_element(*img_aadhar_locator)

    doc_10th.send_keys(marksheet_path)
    sleep(3)
    doc_12th.send_keys(marksheet_path)
    sleep(3)
    doc_LC.send_keys(lc_path)
    sleep(3)
    doc_aadhar.send_keys(aadhar_path)
    sleep(3)


def uplod_button(driver):
    upload_locator = By.ID, "addimage"
    upload = driver.find_element(*upload_locator)
    upload.click()

    assert driver.title == 'View Documents'
    sleep(10)


def find_view_uploaded_docs(driver):
    view_docs_locator = By.LINK_TEXT, "View Uploaded Documents"
    view_docs = driver.find_element(*view_docs_locator)
    view_docs.click()
    sleep(3)


def check_docs(driver):
    images_locator = By.TAG_NAME, "img"
    images = driver.find_elements(*images_locator)

    for image in images:
        doc_10th = image.get_attribute('src')
        get_10th = requests.get(doc_10th)
        assert get_10th.status_code == 200
        print(get_10th)

