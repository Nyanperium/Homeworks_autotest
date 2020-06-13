'''Тестируем яндекс.'''
import requests


def test_response_is_ok(url_param):
    '''Код ответа от сервера должен быть меньше 400.'''

    assert requests.get(url_param).ok
