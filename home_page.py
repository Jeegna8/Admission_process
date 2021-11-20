from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from types import SimpleNamespace
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement


def open_home_page(driver):
    URL = 'http://localhost/admission/fullpro/'
    driver.get(URL)
    driver.maximize_window()
    sleep(3)
    title_locator = By.TAG_NAME, 'p'
    title = driver.find_element(*title_locator)
    assert title.text == "HomePage"





