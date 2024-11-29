def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        try:
            result += i  # Пытаемся добавить элемент
        except TypeError:
            incorrect_data += 1  # Увеличиваем счётчик некорректных данных

    return result, incorrect_data


def calculate_average(numbers):
    # Проверяем, является ли numbers коллекцией
    if not isinstance(numbers, (list, tuple, set)):
        print("В numbers записан некорректный тип данных")
        return None

    # Если коллекция пуста, сразу возвращаем 0
    if len(numbers) == 0:
        return 0

    # Используем personal_sum для подсчёта суммы чисел
    total_sum, incorrect_data = personal_sum(numbers)   # total_sum тот же result после распаковки
    total_count = len(numbers) - incorrect_data

    # Если некорректных данных столько, что считать нечего, возвращаем 0
    return total_sum / total_count if total_count > 0 else 0


# Примеры вызова
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')