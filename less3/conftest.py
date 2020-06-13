import pytest


@pytest.fixture(scope="module")
def start_test_brewery_api(request):
    '''Приветствие из фикстуры.'''
    print('Hi from ', request.module)

    def end_test_brewery_api():
        '''Прощание из фикстуры.'''
        print('Bye from ', request.module)

    request.addfinalizer(end_test_brewery_api)
