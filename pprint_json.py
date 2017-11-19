import json
import os
from pprint import pprint


filename = 'alco_shops.json'


def load_data_json(filename):
    if not os.path.exists(filename):
        return None
    with open (filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def pretty_print_json(filename):
    return pprint(data)


if __name__ == '__main__':
    data = load_data_json(input('Введите название/адрес файл: '))
    pretty_print_json(data)
