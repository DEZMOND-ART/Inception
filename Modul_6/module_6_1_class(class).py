class Animal:   # Животные
    alive = True  # животное живое
    fed = False  # голоден

    def __init__(self, name):
        self.name = name

    def eat(self, food):

        if not isinstance(food, Plant):
            print(f'{self.name} не может съесть это {food}. Это не съедобно!')
            return

        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Plant:    # Растения
    edible = False  # растение несъедобно

    def __init__(self, name):
        self.name = name


class Mammal(Animal):   # Млекопитающие
    pass


class Predator(Animal):     # Хищники
    pass


class Flower(Plant):    # Цветок
    edible = False


class Fruit(Plant):     # Фрукт
    edible = True


a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')


print(a1.name)  # Волк с Уолл-Стрит

print(p1.name)  # Цветик семицветик

print(a1.alive)     # Волк с Уолл-Стрит живой

a1.eat(p1)      # Волк с Уолл-Стрит съел Цветик семицветик

print(a1.alive)     # Волк с Уолл-Стрит погиб

print("-" * 305)      # разделение

print(a2.fed)       # Хатико голодный

a2.eat(p2)      # Хатико съел Заводной апельсин

print(a2.fed)   # Хатико сытый
