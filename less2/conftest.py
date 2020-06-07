import pytest
import time
import random

@pytest.fixture(autouse=True)
def count_time(request):
    start_time = time.time()
    print ('fixture {} start from {}'.format(request.scope, request.node))
    def fin_time():
        print('finally time is ', time.time()-start_time)
    request.addfinalizer(fin_time)

@pytest.fixture(scope='session')
def start_and_end_time(request):
    print('!!!start time is ', time.time(), '!!!')
    def end_time():
        print('!!!end time is ', time.time(), '!!!')
    request.addfinalizer(end_time)

@pytest.fixture(scope='module')
def hi_from_module(request):
    print ('hi!')
    def this_is_end_from_module():
        print ('this is end!')
    request.addfinalizer(this_is_end_from_module)