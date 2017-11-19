import json
import os
from pprint import pprint


json_filename = 'alco_shops.json'


def load_data_json(json_filename):
    if not os.path.exists(json_filename):
        return None
    with open (json_filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def pretty_print_json(json_filename):
    return pprint(json_content)


if __name__ == '__main__':
    json_content = load_data_json(input('Введите название/адрес файл: '))
    pretty_print_json(json_content)
    
