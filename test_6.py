import csv
import argparse


def validate_csv(file_path, has_header=True, delimiter=','):
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f, delimiter=delimiter)

            if has_header:
                # Проверяем наличие заголовка
                header = next(reader)
                if not header:
                    raise ValueError('Missing header in the CSV file.')

            # Проверяем каждую строку в файле
            for row in reader:
                if not row:
                    raise ValueError('Empty row found in the CSV file.')

            print('CSV file is valid.')

    except FileNotFoundError:
        print('File not found.')
        return 1

    except csv.Error as e:
        print('Error reading the CSV file:', str(e))
        return 1

    except ValueError as ve:
        print(str(ve))
        return 1

    return 0


if __name__ == '__main__':
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Validate a CSV file.')

    # Добавляем аргумент для пути к CSV-файлу
    parser.add_argument('file', type=str, help='Path to the CSV file.')

    # Добавляем флаг --no-header для указания отсутствия заголовка
    parser.add_argument('--no-header', action='store_false', dest='has_header',
                        help='Specify if the CSV file does not have a header.')

    # Добавляем аргумент --delimiter для выбора разделителя
    parser.add_argument('--delimiter', type=str, default=',', help='Delimiter used in the CSV file.')

    # Разбираем переданные аргументы командной строки
    args = parser.parse_args()

    # Вызываем функцию validate_csv с переданными аргументами
    exit_code = validate_csv(args.file, has_header=args.has_header, delimiter=args.delimiter)

    # Завершаем скрипт с соответствующим кодом завершения
    exit(exit_code)

#проверка данного кода производилась с помощью команды python test_6.py path/to/file.csv

