import csv

import tablib
import json
from modal import account


def set_file(file_name, in_data):
    f = open(file_name, 'w')
    f.write(in_data)


def get_file_by_name(file_name, key=''):
    with open(file_name, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if key != '' and key in row:
                print(row)


def del_row_by_name(file_name, key=''):
    pass

