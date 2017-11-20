import json
import os


def load_data_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def pretty_print_json(filepath):
    return print(json.dumps(json_content, ensure_ascii=False, indent=4, sort_keys=False))


if __name__ == '__main__':
    try:
        filepath = 'alco_shops.json'
        json_content = load_data_json(filepath)
        pretty_print_json(json_content)
    except (IOError, Exception) as e:
        print("File is empty or not exist")
