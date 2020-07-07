'''Тестируем OpenCart'''

def test_one(driver, adress_param):
    '''Переходим на страницу OpenCart и проверяем, что мы находимся на ней.'''
    driver.get(adress_param)
    assert driver.find_element_by_xpath('/html/body/footer/div/p/a').text == 'OpenCart'
