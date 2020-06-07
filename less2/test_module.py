'''Этот модуль содержит 5 функций и 11 проверок к ним.'''
import random
import pytest


def generate_list():
    '''Эта функция генерирует список из 10 значение в диапазоне от 1 до 200.'''
    our_list = [random.randint(1, 200) for x in range(10)]
    print('hi from generate_list()', our_list)
    return our_list


def append_to_list(our_list):
    '''Эта функция добавляет к списку случайное значение от 200 до 400.'''
    our_list.append(random.randint(200, 400))
    print('hi from append_to_list()', our_list)
    return our_list


def sum_two_strings(string_one, string_two):
    '''Эта функция суммирует 2 строки.'''
    return str(string_one) + str(string_two)


def sum_two_integers(int_one, int_two):
    '''Эта функция суммирует 2 целых числа.
    При вводе неккоректных значиений просит ввести целые числа.'''
    try:
        return int(int_one) + int(int_two)
    except (TypeError, ValueError):
        return 'Введите целые числа.'


def hello_word_name(name):
    '''Эта функция возвращает приветствие с именем, которое мы передали.'''
    return 'Hello word, im {}!'.format(name)


@pytest.mark.parametrize('function_for_check', [generate_list()])
def test_len(function_for_check, hi_from_module):
    '''Этот тест проверяет, что длина списка, полученного из функции generate_list(), равна 10.'''
    assert len(function_for_check) == 10


def test_len_2(function_for_check=append_to_list(generate_list())):
    '''Этот тест проверяет,
    что длина списка, полученного из функции append_to_list(generate_list()), равна 10.'''
    assert len(function_for_check) == 11


def test_value_generate_function_is_int(function_for_check=generate_list()):
    '''Этот тест проверяет,
    что случайное значение, полученное из функции generate_list() является int.'''
    assert isinstance(function_for_check[random.randint(0, 9)], int)


def test_value_generate_function(function_for_check=generate_list()):
    '''Этот тест проверяет,
    что случайное значение, полученное из функции generate_list(), меньше/равно 200.'''
    assert function_for_check[random.randint(0, 9)] <= 200


def test_value_append_function(function_for_check=append_to_list(generate_list())):
    '''Этот тест проверяет, что последнее значение,
     полученное из функции append_to_list(generate_list()), больше/равно 200.'''
    assert function_for_check[-1] >= 200


@pytest.mark.parametrize('two_strings', [[14.2, '2'], ['adf2sc', 12]])
def test_string_function_type(two_strings, start_and_end_time):
    '''Этот тест проверяет, что результат выполения функции sum_two_strings() это str.'''
    [string_one, string_two] = two_strings
    assert isinstance(sum_two_strings(string_one, string_two), str)


@pytest.mark.parametrize('two_strings', [[1, 2], ['ee', 12], ['ewdf', 'sfs'], [None, 12]])
def test_string_function_value(two_strings):
    '''Этот тест проверяет,
     что результат выполения функции sum_two_strings() это строка, состоящая из 2 исходных.'''
    function_for_check = sum_two_strings(two_strings[0], two_strings[1])
    assert function_for_check == str(two_strings[0]) + str(two_strings[1])


@pytest.mark.parametrize('two_integers', [[1, 2], ['1', 12], ['0', '12']])
def test_int_function_value_positive(two_integers):
    '''Этот тест проверяет,
     что результат выполения функции sum_two_integers() это сумма двух переданных аргументов.'''
    function_for_check = sum_two_integers(two_integers[0], two_integers[1])
    assert function_for_check == int(two_integers[0]) + int(two_integers[1])


@pytest.mark.parametrize('two_integers', [['fds', 'sd'], [None, 14]])
def test_int_function_value_negative(two_integers):
    '''Этот тест проверяет,
    что результат выполения функции sum_two_integers() при неккоректных аргументах.
    Должна появиться подсказка.'''
    function_for_check = sum_two_integers(two_integers[0], two_integers[1])
    assert function_for_check == 'Введите целые числа.'


@pytest.mark.parametrize('names', ['Jim', 'Elly'])
def test_hello_word_name_value(names):
    '''Этот тест проверяет,
    что результат выполения функции hello_word_name() это приветствие с именем.'''
    assert hello_word_name(names) == 'Hello word, im {}!'.format(names)


@pytest.mark.parametrize('names', ['Ann', 'Georgie'])
def test_hello_word_name_type(names):
    '''Этот тест проверяет, что результат выполения функции hello_word_name() это строка.'''
    assert isinstance(hello_word_name(names), str)
