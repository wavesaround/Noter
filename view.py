from datetime import datetime


def launch():
    print('Привет. Это Noter')
    print('Для продолжения введите цифру\n')
    print('1 - Список заметок\n2 - Добавить заметку\n3 - Найти заметку\n4 - Изменить заметку\n5 - Удалить заметку')


def type_data(message):
    return input(f'{message}')


def print_search(notes: list):

    for row in notes:
        print(*(x + ' : ' + y + ' ' for x, y in row.items()))

