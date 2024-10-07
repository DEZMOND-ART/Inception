calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return string.lower(), string.upper(), len(string)


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    search_to_lower = [index.lower() for index in list_to_search]
    return string in search_to_lower


# comfortable reading
separator = '-' * 305

# Test 1
print(separator)
print(string_info('Dodger'))
print(string_info('Fell'))
print(string_info('Tramp'))
print(string_info('Dog'))
print(separator)

# Test 2
print(is_contains('POE', ['afk', 'Build', 'CWDT', 'poE']))
print(is_contains('blender', ['designer', 'modeler', 'artist']))
print(separator)

# Number of uses
print('number of uses of functions def:', calls)
print(separator)
