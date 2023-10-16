import random
import csv


def generate_data(N, header):
    # Проверяем корректность переданного значения N
    if N < 1 or N > 100:
        raise ValueError('Invalid value for N. N should be between 1 and 100.')

    # Создаем список заголовков из ключей словаря header
    headers = list(header.keys())

    # Проверяем наличие заголовка
    if not headers:
        raise ValueError('Empty header. Header should contain at least one column.')

    # Открываем файл для записи данных
    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)

        # Записываем заголовок в файл
        writer.writerow(headers)

        # Генерируем N строк данных
        for _ in range(N):
            row_data = []

            # Генерация значения для каждой колонки
            for column in headers:
                column_type = header[column]

                if column_type == int:
                    # Генерация случайного целого числа от 0 до 100
                    value = random.randint(0, 100)
                elif column_type == str:
                    # Генерация случайной строки длиной не более 100 символов
                    value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                                   k=random.randint(1, 100)))
                elif column_type == bool:
                    # Генерация случайного булева значения
                    value = random.choice([True, False])
                else:
                    raise ValueError(
                        f'Invalid column type for column "{column}". Supported types are int, str, and bool.')

                row_data.append(value)

            # Записываем строку данных в файл
            writer.writerow(row_data)

    print(f'{N} rows of data have been generated and saved to output.csv.')


# Пример использования функции generate_data
header = {'Column1': int, 'Column2': str, 'Column3': bool}
generate_data(10, header)
