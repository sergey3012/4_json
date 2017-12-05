import json


def load_data_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def pretty_print_json(json_data):
    return print(json.dumps(json_data, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    try:
        filepath = input('Введите адрес файла: ')
    except (FileNotFoundError, PermissionError) as ex:
        print('Ошибка доступа: файл не существует ')
    except ValueError as ex:
        print('Ошибка json данных!')
    finally:
        pretty_json = pretty_print_json(load_data_json(filepath))
        pretty_print_json(pretty_json)
