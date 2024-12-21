def all_variants(text):
    length = len(text)
    for r in range(1, length + 1):
        for i in range(length - r + 1):
            yield text[i:i + r]


a = all_variants("abc")


for i in a:
    print(i)