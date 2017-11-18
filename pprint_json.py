import json
import os
from pprint import pprint


filename = 'alco_shops.json'


def load_data(filename):
    if not os.path.exists(filename):
        return None
    with open (filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def pretty_print_json(filename):
        return pprint(data)


if __name__ == '__main__':
    data = load_data(input('Введите название/адрес файла: '))
    pretty_print_json(data)
