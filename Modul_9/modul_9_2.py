first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
# >=5
first_result = [len(s) for s in first_strings if len(s) >= 5]
# Список кортежей из слов одинаковой длинны
second_result = [(f, s) for f in second_strings for s in second_strings if len(f) == len(s)]
# Словарь, где ключ - строка, а значение - длинна слова. Только четные
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}


# Вывод
print(first_result)

print(second_result)

print(third_result)