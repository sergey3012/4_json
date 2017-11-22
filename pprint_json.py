import json
import sys


def load_data_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def pretty_print_json(json_data):
    if json_data:
        return print(json.dumps(json_data, ensure_ascii=False, indent=4, sort_keys=False))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('\nУкажите файл в формате json.\n'
              'python test.py <path to file>')
        exit()
    try:
        pretty_json = pretty_print_json(load_data_json(sys.argv[1]))
        print(pretty_json)
    except (FileNotFoundError, PermissionError) as ex:
        print('\nОшибка доступа: файл не существует '
              'или недоступен для чтения.\n' + str(ex))
    except ValueError as ex:
        print('\nОшибка json данных!\n' + str(ex))
