my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# прописывается для последующего изменения данного значения index += 1
index = 0
# цикл выполняется пока длинна списка больше индекса
# т.е. когда 12 == 11 + 1 значение поменяется на folse и цикл остановится
while len(my_list) > index:
    # записываем непосредственно само число, при первом прохождении это 42
    number = my_list[index]
    # проверяем 42 < 0 (нет проверяем следующее условие) и т.д.
    if number < 0:
        # если значение отрицательное цыкл завершается
        break
    # проверяем 0 == 0
    elif number == 0:
        # переходим к следующему значению
        index += 1
        # игнарируем код ниже continue если number == 0
        continue
    # в случае если number > 0 выводим его на экран
    print(number)
    # переходим к следующему значению
    index += 1
