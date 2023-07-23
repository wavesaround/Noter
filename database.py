from pathlib import Path
import csv
import os
from view import alert_return

db_path = Path('database.csv')


def check_empty():
    if os.path.getsize(db_path) == 0:
        with open(db_path, 'w', encoding='utf-8') as csvfile:
            csvfile.writelines(f'id;title;note;date;time\n')
    else:
        pass


def write_to_db(new_dict: dict):
    fieldnames = ['id', 'title', 'note', 'date', 'time']
    with open(db_path, 'a', encoding='utf-8') as db_main:
        writer = csv.DictWriter(db_main, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE)
        writer.writerow(new_dict)


def get_id() -> int:
    with open(db_path, 'r', encoding='utf-8') as db:
        reader = csv.DictReader(db, delimiter=';')
        ids = []
        for row in reader:
            ids.append(row['id'])
        if not ids:
            return 1
        else:
            return int(max(ids)) + 1


def search_data(data: str) -> list:
    search_result = []
    new_data = data.replace(' ', ';').lower()
    with open(db_path, 'r', newline='') as db_main:
        reader = csv.reader(db_main, delimiter=';')
        for row in reader:
            if new_data in row:
                search_result.append(row)
        return search_result


def get_all() -> list:
    with open(db_path, 'r', encoding='utf-8') as db:
        reader = csv.DictReader(db, delimiter=';')
        rows = []
        for row in reader:
            rows.append(row)
    return rows


def get_one(note_id: int):
    with open(db_path, 'r', encoding='utf-8') as db:
        reader = csv.DictReader(db, fieldnames=None, delimiter=';')
        for row in reader:
            if row['id'] == note_id:
                return row


def delete_card(str_target: str):
    with open(db_path, 'r') as db_read:
        lines = db_read.readlines()
    with open(db_path, 'w') as db_write:
        for line in lines:
            if line == str_target:
                pass
            else:
                db_write.write(line)


def edit_one(new_row):
    fieldnames = ['id', 'title', 'note', 'date', 'time']
    with open(db_path, 'r', encoding='utf-8') as db_read:
        reader = csv.DictReader(db_read, fieldnames=fieldnames, delimiter=';')
        rows = list(reader)
    with open(db_path, 'w', encoding='utf-8') as db_write:
        writer = csv.DictWriter(db_write, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in rows:
            if row['id'] == new_row['id']:
                writer.writerow(new_row)
            else:
                writer.writerow(row)
    alert_return(True)

def delete_note(param):
    return None