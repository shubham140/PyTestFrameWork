import pytest

from Pages.Login_Page import Login_Page
from Tests.Test_Base import Test_Base
from Tests import Config_Fixture


class Test_Login(Test_Base):

    def test_login(self):
        self.login = Login_Page(self.driver)
        self.login.login()
        assert True
