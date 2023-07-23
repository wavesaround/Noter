import view
import database as db
from datetime import datetime


def new_note():
    note_id = db.get_id()
    title = view.type_data('Введите заголовок: ')
    note = view.type_data('Введите тело заметки: ')
    date = datetime.today().strftime("%d-%m-%Y")
    time = datetime.today().strftime("%H:%M:%S")
    new_dict = {
        'id': note_id,
        'title': title,
        'note': note,
        'date': date,
        'time': time
    }
    db.write_to_db(new_dict)


def open_note():
    note_id = view.type_data('Введите id заметки\n')
    get_row = db.get_one(note_id)
    view.print_one(get_row)


def open_list():
    get_row = db.get_all()
    view.print_search(get_row)
    match view.action_menu():
        case 'open':
            open_note()
        case 'edit':
            edit_note()
        case 'del':
            delete_note()
        case _:
            print('ОШИБКА: Неверный ключ\n')
            start()


def edit_note():
    note_id = view.type_data('Введите id заметки\n')
    get_row = db.get_one(note_id)
    get_row['note'] = view.type_note(get_row['note'])
    get_row['date'] = datetime.today().strftime("%d-%m-%Y")
    get_row['time'] = datetime.today().strftime("%H:%M:%S")
    db.edit_one(get_row)


def delete_note():
    note_id = view.type_data('Введите id заметки\n')
    view.sure('delete')



def start():
    db.check_empty()
    view.launch()
    go_button = view.type_data('')
    match go_button:
        case '1':
            open_list()
        case '2':
            new_note()
        case '3':
            edit_note()
        case '4':
            delete_note()
        case _:
            print('Попробуйте еще')
            start()
