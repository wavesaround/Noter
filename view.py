from datetime import datetime


def launch():
    print('Привет. Это Noter')
    print('Для продолжения введите цифру\n')
    print('1 - Список заметок\n2 - Добавить заметку\n3 - Изменить заметку\n4 - Удалить заметку')


def type_data(message):
    return input(f'{message}')


def print_search(notes: list):
    list_sort = sorted(
        notes,
        key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'), reverse=True
    )
    for row in list_sort:
        print(*(x + ' : ' + y + ' ' for x, y in row.items()))

