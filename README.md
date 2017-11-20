# Prettify JSON

This script on the input takes the path to a file with arbitrary data in JSON format and displays its contents in the console in an easy-to-read form: adds line breaks, left indents and spaces.

# Quickstart

To run the script:
```
$ python pprint_json.py [alco_shops.json]
```

# Example of result
```python
python pprint_json.py example.json
[
    {
        "Number": 1,
        "Cells": {
            "ClarificationOfWorkingHours": null,
            "Address": "улица Академика Павлова, дом 10",
            "TypeService": "реализация продовольственных товаров",
            "IsNetObject": "да",
            "WorkingHours": [
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "понедельник"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "вторник"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "среда"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "четверг"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "пятница"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "суббота"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "воскресенье"
                }
            ]                                                          
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
