from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from types import SimpleNamespace
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from driver_call import *


def open_home_page(driver):
    homepage_url = "http://localhost/admission/fullpro/home_page/homepage.html"
    driver.get(homepage_url)
    sleep(2)


def open_admin_page(driver):
    admin_module_locator = By.LINK_TEXT, "Admin"
    admin_module = driver.find_element(*admin_module_locator)
    admin_module.click()
    sleep(2)


def open_counsellor_page(driver):
    counsellor_module_locator = By.LINK_TEXT, "Councellor"
    counsellor_module = driver.find_element(*counsellor_module_locator)
    counsellor_module.click()
    sleep(2)


def open_student_page(driver):
    student_module_locator = By.LINK_TEXT, "Student"
    student_module = driver.find_element(*student_module_locator)
    student_module.click()
    sleep(2)
