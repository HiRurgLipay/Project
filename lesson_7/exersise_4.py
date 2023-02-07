import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f'Время выполнения функции {func.__name__}: {end_time} секунд')
        return result

    return wrapper


@decorator
def sum_numbers(a, b):
    return a + b


@decorator
def multiply_numbers(a, b):
    return a * b


sum_numbers(2, 3)








