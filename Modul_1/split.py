def split_word(example):                                                                # создаем функцию разбить_слово
    length = len(example)                                                               # сохраняет результат в виде целого числа
    split_index = (length - 1) // 2 + 1                                                 # матем. операция по отделению половины слова и приводящее ее к нечетному значению
    second_half = example[split_index:]                                                 # присвоение результата к переменной вторая половина
    return second_half                                                                  # Возвращение результата
example = input("Введите слово: ")                                                      # ввод переменной с которой будет вестить работа
second_half = split_word(example)                                                       # присвоение конечного результата к переменной example которую только что ввели
print(f"{example[0]}\n{example[-1]}\n{second_half}\n{example[::-1]}\n{example[1::2]}")  # вывод результатов на экран