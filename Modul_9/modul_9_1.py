def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([7, 6, 1, 8, 5, 4, 3, 9, 2], max, min))
print(apply_all_func([7, 6, 1, 8, 5, 4, 3, 9, 2], len, sum, sorted))
