def find_in_different_registers(words):
    # Создаем множество для хранения уникальных слов в нижнем регистре
    unique_words = set()

    # Создаем множество для хранения слов, у которых есть дубликаты по регистру
    duplicate_words = set()

    for word in words:
        # Приводим слово к нижнему регистру для проверки дубликатов
        lower_word = word.lower()

        if lower_word in unique_words:
            # Если слово уже находится в множестве unique_words, то добавляем его в множество duplicate_words
            duplicate_words.add(lower_word)
        else:
            # Если слово не является дубликатом, добавляем его в множество unique_words
            unique_words.add(lower_word)

    # Удаляем из unique_words все слова, которые есть в duplicate_words
    unique_words -= duplicate_words

    # Возвращаем отсортированный список уникальных слов в нижнем регистре
    return sorted(list(unique_words))


words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
print(find_in_different_registers(words))
