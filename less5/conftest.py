import pytest
from selenium import webdriver
from variables import *


def pytest_addoption(parser):
    '''Добавляем параметры адресс сайта и браузер,
    получаемые из командной строки, для запуска тестов'''
    parser.addoption('--address', action='store', default=opencart_adress)
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture
def adress_param(request):
    '''Получаем параметр адрес сайта, введенный в командную строку.'''
    return request.config.getoption('--address')


@pytest.fixture
def browser_param(request):
    '''Получаем параметр браузер, введенный в командную строку.'''
    return request.config.getoption('--browser')


@pytest.fixture
def driver(request, browser_param):
    '''Открываем и закрываем браузер с заданными опциями.'''
    if browser_param.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--start-fullscreen')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        wd = webdriver.Chrome(options=options)
    elif browser_param.lower() == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--kiosk')
        options.add_argument('--headless')
        wd = webdriver.Firefox(options=options)
    elif browser_param.lower() == 'ie':
        options = webdriver.IeOptions()
        wd = webdriver.Ie(options=options)
    request.addfinalizer(wd.quit)
    return wd
