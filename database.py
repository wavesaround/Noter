from pathlib import Path
import csv
import os

db_path = Path('database.csv')

# def check_empty():
#     if os.path.getsize(db_path) == 0:
#         with open('names.csv', 'w', newline='', encoding='utf-8') as csvfile:
#             fieldnames = ['id', 'title', 'note', 'date', 'time']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
#             writer.writeheader()
#             writer.writerow({'id': '1', 'title': 'test'})
#     else:
#         pass


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

