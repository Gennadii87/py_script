# TODO: Задание 1
"""
1. Подключение к API и получение данных
Напишите скрипт на Python, который подключается к API и получает данные.
Например, используйте публичное API https://jsonplaceholder.typicode.com/posts.
Сохраните полученные данные в формате JSON в файл.

"""
import requests
import json


def get_json():
    url = 'https://jsonplaceholder.typicode.com/posts'
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open('json_data.json', 'w', encoding='utf-8') as file:
                json.dump(response.json(), file, ensure_ascii=False, indent=4)
        else:
            return response.text
    except requests.exceptions.RequestException as e:
        return False, str(e)


if __name__ == '__main__':
    get_json()
