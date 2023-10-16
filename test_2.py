# Подключаем все необходимые модули
import functools
import logging
import time


def cache_and_log_execution_time(cache_limit=3):
    def decorator(func):
        # Создаем кеш для хранения результатов вызовов функции
        cache = {}
        call_count = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_count
            # Генерируем уникальный ключ на основе аргументов функции
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                # Используем сохраненный результат из кеша
                logging.info(f"Using cached result for {func.__name__}({args}, {kwargs})")
                return cache[key]

            call_count += 1
            start_time = time.time()
            # Вызываем функцию и получаем результат
            result = func(*args, **kwargs)
            end_time = time.time()

            # Сохраняем результат в кеше
            cache[key] = result

            if call_count % cache_limit == 0:
                # Обновляем кеш после определенного количества вызовов функции
                logging.info(f"Cache updated for {func.__name__}")

            # Выводим информацию о времени выполнения функции
            logging.info(f"{func.__name__} took {end_time - start_time} seconds to execute")

            return result

        return wrapper

    return decorator


import logging

# Настраиваем модуль логирования для вывода информации
logging.basicConfig(level=logging.INFO)


@cache_and_log_execution_time(cache_limit=3)
def calculate_square(x):
    time.sleep(1)  # Имитация долгой работы
    return x ** 2


print(calculate_square(5))
print(calculate_square(5))
print(calculate_square(6))
print(calculate_square(6))
print(calculate_square(7))
