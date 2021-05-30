import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome"],scope="class")
def ini_driver(request):
    if(request.param=="chrome"):
        web_driver=webdriver.Chrome(ChromeDriverManager().install())

    request.cls.driver=web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.quit()



