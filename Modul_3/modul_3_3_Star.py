def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
# Так и не понял почему выделяет (b=25) и (c=[1, 2, 3]).
# Из за повторного использования переменной?
print_params(b=25)

print_params(c=[1, 2, 3])

values_list = [4, 5.5, 'digital']

values_dict = {'a': 1, 'b': 'строка', 'c': False}

print_params(*values_list)

print_params(**values_dict)

values_list_2 = ('Пантеон', 2.2)

print_params(*values_list_2, 42)