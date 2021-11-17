from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from types import SimpleNamespace
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    # Go to website
    driver.get("http://localhost/admission/fullpro/home_page/homepage.html")
    return driver



