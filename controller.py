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


def open_list():
    pass


def edit_note():
    pass


def delete_note():
    pass


def start():
    view.launch()
    go_button = input('')
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
