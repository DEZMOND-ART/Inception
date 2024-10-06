import random


def stone():
    n = random.choice(range(3,21))
    print(f'число на первом камне: {n}')
    result = []
    for a in range(1,21):
        for b in range(a + 1, 21):
            if n % (a + b) == 0:
                result.append(str(a))
                result.append(str(b))
    print(f'{n} - {"".join(result)}')
    stone()
