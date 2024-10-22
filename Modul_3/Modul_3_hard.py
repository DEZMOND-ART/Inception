def calculate_structure_sum(*args):
    result = 0

    # Проверяет элементы рекурсивно - грубо говоря открывает капот
    for i in args:
        if isinstance(i, (list, tuple, set)):  # Если i - список, кортеж или множество
            result += calculate_structure_sum(*i)  # Достает i из data_structure и + к result
        elif isinstance(i, dict):  # Если i - словарь
            result += calculate_structure_sum(*i.keys())  # + ключи
            result += calculate_structure_sum(*i.values())  # + значения
        elif isinstance(i, (int, float)):  # Если i - число
            result += i  # + число
        elif isinstance(i, str):  # Если i - строка
            result += len(i)
    return result


# Пример тестирования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

test = calculate_structure_sum(*data_structure)
print(f"Сумма чисел и символов: {test}")
