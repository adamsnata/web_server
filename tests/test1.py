import os
import re
from collections import defaultdict


def count_requests():
    current_directory = os.path.dirname(__file__)
    log_file_path = os.path.join(current_directory, 'resource', 'access1.log')

    # Инициализируем словарь для подсчета запросов по методам
    methods_count = defaultdict(int)
    http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']

    # Регулярное выражение для поиска методов
    method_regex = re.compile(r'\"(GET|POST|PUT|DELETE|OPTIONS|HEAD) ')

    with open(log_file_path, 'r') as file:
        lines = file.readlines()
        request_count = len(lines)
        for line in lines:
            match = method_regex.search(line)
            if match:
                method = match.group(1)
                methods_count[method] += 1

    # Выводим количество запросов на экран
    print(f"Total requests: {request_count}")
    # Выводим количество запросов по методам на экран
    for method in http_methods:
        print(f"{method} - {methods_count[method]}")

def test1():
    count_requests()
