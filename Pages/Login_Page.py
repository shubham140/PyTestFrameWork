from Config import Base_Config
from Pages.Base_Page import Base_Page
from selenium.webdriver.common.by import By

class Login_Page(Base_Page):
    """This Page Object Repo"""

    user_name=(By.XPATH,"//*[@id='txtUsername']")
    password=(By.XPATH,"//*[@id='txtPassword']")
    login_button=(By.XPATH,"//*[@name='Submit']")



    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(Base_Config.URL)

    def login(self):
        self.enter_details(Login_Page.user_name,"admin",30)
        self.enter_details(Login_Page.password,"Admin123",30)
        self.do_click(Login_Page.login_button,10)

