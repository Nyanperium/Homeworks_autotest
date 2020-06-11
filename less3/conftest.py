import pytest
from test_brewery_api import APIClient


@pytest.fixture(scope="module")
def start_test_brewery_api(request):
    print ('Hi from ', request.module)
    def end_test_brewery_api():
        print ('Bye from ', request.module)
    request.addfinalizer(end_test_brewery_api)
