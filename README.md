# Prettify JSON

This script on the input takes the path to a file with arbitrary data in JSON format and displays its contents in the console in an easy-to-read form: adds line breaks, left indents and spaces.

# Quickstart

To run the script:
```
$ python pprint_json.py [alco_shops.json]
```

In case the file does not exist, the script will return:

```python
      if not os.path.exists(filename):
        return None
```



# Example of result
```python
                                                              {'DayOfWeek': 'пятница',
                                                               'Hours': '09:00-22:00'},
                                                              {'DayOfWeek': 'суббота',
                                                               'Hours': '09:00-22:00'},
                                                              {'DayOfWeek': 'воскресенье',
                                                               'Hours': '09:00-22:00'}],
                                             'global_id': 25173101},
                              'DatasetId': 1854,
                              'ReleaseNumber': 2,
                              'RowId': '4cfabe8c-1eea-4dc2-81a0-99ddb0ff3e35',
                              'VersionNumber': 1},
               'type': 'Feature'},
              {'geometry': {'coordinates': [37.521364353495464,
                                            55.541676236353744],
                            'type': 'Point'},
               'properties': {'Attributes': {'Address': 'улица Адмирала '
                                                        'Лазарева, дом 43',
                                             'AdmArea': 'Юго-Западный '
                                                        'административный '
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
