
"""So here i will be writing all generic fucntions required for my POM Framework"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page:

    def __init__(self,driver):
        self.driver=driver


    def do_click(self,by_locator,time):
        wait=WebDriverWait(self.driver,time)
        wait.until(ec.visibility_of_element_located(by_locator)).click()

    def enter_details(self,by_locator,text,time):
        WebDriverWait(self.driver,time).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self,title,time):
        WebDriverWait(self.driver,time).until(ec.title_is(title))
        return self.driver.title


