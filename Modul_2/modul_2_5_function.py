def get_matrix(n, m, value):
    return [[value for _ in range(m)] for _ in range(n)]
    # matrix = []
    # for _ in range(n):
    #     line = []
    #     matrix.append(line)
    #     for _ in range(m):
    #         line.append(value)
    # return matrix


# Тест
result1 = get_matrix(1, 1, 1)
result2 = get_matrix(2, 2, 2)
result3 = get_matrix(3, 3, 3)

print(result1)
print(result2)
print(result3)
