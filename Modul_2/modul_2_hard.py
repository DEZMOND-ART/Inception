import random


def stone():
    n = random.choice(range(3, 21))
    result = []
    for a in range(1, n // 2 + 1):
        for b in range(a + 1, n - a + 1):
            if n % (a + b) == 0:
                result += str(a) + str(b)
    print(f'число на первом камне: {n}')
    print(f'{n} - {"".join(result)}')


stone()
