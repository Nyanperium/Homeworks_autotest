'''Тестируем OpenCart'''


def test_one(driver):
    '''Переходим на страницу OpenCart и проверяем, что мы находимся на ней.'''
    driver.get('http://192.168.0.101/opencart/')
    assert driver.find_element_by_xpath('/html/body/footer/div/p/a').text == 'OpenCart'
