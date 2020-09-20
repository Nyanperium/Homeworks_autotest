import pytest
from selenium import webdriver
from variables import *

def pytest_addoption(parser):
    parser.addoption('--address', action='store', default=opencart_adress)
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture
def adress_param(request):
    return request.config.getoption('--address')


@pytest.fixture
def browser_param(request):
    return request.config.getoption('--browser')

@pytest.fixture
def driver(request, browser_param):
    if browser_param.lower() == 'chrome':
        wd=webdriver.Chrome()
    elif browser_param.lower() == 'firefox':
        wd=webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd