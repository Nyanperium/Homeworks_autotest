'''Генерация данных для проекта.'''
import csv
import random
import re


def get_data_from_csv_to_dict(path):
    '''Считываем данные о пользователях из csv файла. Записываем их в словарь.

    Приводим ФИО к читаемому виду. Удаляем пустые данные.'''
    data_dict = {'Name': set(),
                 'City': set(),
                 'Credit_card': set(),
                 'Contribution': set(),
                 'Mortgage': set()}
    with open(path) as file:
        data = csv.reader(file)
        for row in data:
            if row[0] == 'ФИО':
                continue
            for i in range(5):
                if i == 0:
                    data_dict[list(data_dict.keys())[i]].add(re.match(r'\S+ \S+ \w+',
                                                                      row[i]).group())
                else:
                    data_dict[list(data_dict.keys())[i]].add(row[i])
        for key in list(data_dict.keys()):
            data_dict[key] = set(filter(None, data_dict[key]))
    return data_dict


def write_csv_with_100_people(data_dict):
    '''На основе словаря с данными пользователей генерируем 100 новых пользователей.'''
    with open('result.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('ФИО', 'Город', 'Кредитная карта', 'Вклад', 'Ипотека'))
        counter = 0
        while counter < 100:
            a_pen.writerow([random.choice(x) for x in (list(data_dict['Name']),
                                                       list(data_dict['City']),
                                                       list(data_dict['Credit_card']),
                                                       list(data_dict['Contribution']),
                                                       list(data_dict['Mortgage']))])
            counter += 1


def main():
    '''Главная функция'''
    write_csv_with_100_people(get_data_from_csv_to_dict('data.csv'))


if __name__ == '__main__':
    main()
