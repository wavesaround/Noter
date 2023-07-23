import sys
from datetime import datetime
from sys import exit
import keyboard


def launch():
    print('Привет. Это Noter')
    print('Для продолжения введите цифру\n')
    print('1 - Список заметок\n2 - Добавить заметку\n3 - Изменить заметку\n4 - Удалить заметку')


def type_data(message):
    return input(f'{message}')


def print_one(row):
    print(f"\n{row['title']}")
    print('–––––––––––––––')
    print(f"{row['note']}\n")
    print('Дата последнего изменения:')
    print(f'{row["date"]} / {row["time"]}')

def print_search(notes: list):
    list_sort = sorted(
        notes,
        key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'), reverse=True
    )
    for row in list_sort:
        print(*(x + ' : ' + y + ' ' for x, y in row.items()))


def alert_return(flag):
    match flag:
        case True:
            return print('Все получилось')
        case _:
            return print('Не получилось')


def sure(question):
    match question:
        case 'edit':
            type_que = ', что хотите изменить заметку?'
        case 'delete':
            type_que = ', что хотите удалить заметку'
        case _:
            type_que = '?'
    user_type = input(f'Вы уверены{type_que}? Y / N: ').lower()
    if user_type == 'y':
        pass
    else:
        exit()


def set_id():
    print('Введите id заметки для дальнейшего действия')
    return input('–>')


def action_menu():
    print(
        'Открыть заметку, введите open\n'
        'Изменить заметку, введите edit\n'
        'Удалить заметку, введите del'
    )
    return input('--> ')


def type_note(input_text):
    # input(keyboard.write(input_text, delay=0, restore_state_after=False, exact=None))
    print(input_text)
    return input('\n')
