import os


def count_requests():
    current_directory = os.path.dirname(__file__)
    log_file_path = os.path.join(current_directory, 'resource', 'access1.log')

    with open(log_file_path, 'r') as file:
        lines = file.readlines()
        request_count = len(lines)

    # Выводим количество запросов на экран
    print(f"Total requests: {request_count}")

def test1():
    count_requests()
