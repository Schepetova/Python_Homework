nums = [1, 2, 3, 4, 5.5, 6, 5.5]


def duplicate_nums(nums):  # заголовок функции, принимает список чисел nums
    duplicates = []  # создается пустой список для хранения чисел
    for num in nums:
        if nums.count(num) == 2 and num not in duplicates:
            duplicates.append(num)  # если число дубликат и не было добавлено в список, то добавляется
    if duplicates:
        return sorted(duplicates)
    else:
        return None  # если нет дубликатов, возвращаем None


print(duplicate_nums(nums))
