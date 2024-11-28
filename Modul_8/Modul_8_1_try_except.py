def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


a = "С Новым Годом "
b = 2025
print(add_everything_up(a, b))

print(add_everything_up(123.456, ' строка'))

print(add_everything_up('яблоко ', 4215))

print(add_everything_up(123.456, 7))