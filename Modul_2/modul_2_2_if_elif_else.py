first = input('Ведите значение для сравнения: ')
second = input('Ведите значение для сравнения: ')
third = input('Ведите значение для сравнения: ')
if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')
