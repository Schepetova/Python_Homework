import tempfile

class TempFileManager:
    def __enter__(self):
        # Создаем временный файл и открываем его в режиме чтения и записи
        self.file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Закрываем файл
        self.file.close()

        # Читаем содержимое файла
        with open(self.file.name, 'r') as f:
            content = f.read()

            # Выводим содержимое файла в консоль
            print(f"Содержимое файла:\n{content}")

            # Выводим количество символов в файле
            print(f"Количество символов в файле: {len(content)}")

        # Удаляем временный файл
        self.file.delete = True

    def repeat(self):
        # Дублируем текущее содержимое файла и добавляем в конец файла
        with open(self.file.name, 'a') as f:
            f.write(open(self.file.name).read())

    def write(self, msg):
        # Записываем текст в начало файла
        with open(self.file.name, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(msg)
            f.write(content)

    def show(self):
        # Выводим содержимое файла в консоль
        with open(self.file.name, 'r') as f:
            content = f.read()
            print(f"Содержимое файла:\n{content}")


# Пример использования контекстного менеджера
with TempFileManager() as manager:
    # Записываем текст в начало файла
    manager.write("Hello, World!")

    # Дублируем содержимое файла и добавляем в конец
    manager.repeat()

    # Выводим содержимое файла в консоль
    manager.show()
