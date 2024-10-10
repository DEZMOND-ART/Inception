first = input('Введите значение для сравнения: ')
second = input('Введите значение для сравнения: ')
third = input('Введите значение для сравнения: ')
if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')
