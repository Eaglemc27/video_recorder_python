import pytest
from selenium import webdriver
from selene.tools import get_driver, set_driver


@pytest.fixture(scope='class')
def setup(request):
    set_driver(webdriver.Chrome('/home/sergey/chromedriver'))

    def teardown():
        get_driver().quit()

    request.addfinalizer(teardown)


@pytest.mark.usefixtures("setup")
class BaseTest(object):
    pass