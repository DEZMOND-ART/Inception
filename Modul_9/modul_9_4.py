import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda f, s: f == s, first, second))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with (open(file_name, 'a', encoding='utf-8') as
f):
            for data in data_set:
                f.write(f'{data}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

ball = MysticBall(['Да', 'Нет', 'Возможно', 'Определённо', 'Никогда'])
print(ball())