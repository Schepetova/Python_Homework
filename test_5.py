class ChainSum:
    def __init__(self, value):
        # Инициализация объекта ChainSum с начальным значением
        self.value = value

    def __call__(self, num=None):
        if num is None:
            # Если не передано новое число, возвращаем текущее значение
            return self.value
        else:
            # Если передано новое число, создаем новый экземпляр ChainSum с обновленным значением
            return ChainSum(self.value + num)


def chain_sum(value):
    # Создание объекта ChainSum с начальным значением
    return ChainSum(value)


# Примеры использования
print(chain_sum(5)())  # 5
print(chain_sum(5)(2)())  # 7
print(chain_sum(5)(100)(-10)())  # 95
