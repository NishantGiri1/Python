"""Q2. Write a decorator that measures the execution time of a function and logs the result to a file."""

import time


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        with open("log.txt", "a") as log_file:
            log_file.write(f"{func.__name__} took {execution_time} seconds to execute\n")

        return result

    return wrapper


# provide the path of the file you want to analyze
file_path = r"wordCountFile.txt"


@log_execution_time
def read_file(path):
    with open(path, "r") as file:
        contents = file.read()
    return contents


file_contents = read_file("wordCountFile.txt")
