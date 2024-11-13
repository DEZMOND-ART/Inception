class Animal:   # Животные
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = True      # животное живое
        self.fed = False       # голоден


class Plant:    # Растения
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = False    # растение несъедобно


class Mammal(Animal):   # Млекопитающие
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Predator(Animal):     # Хищники

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Flower(Plant):    # Цветок
    def __init__(self, name):
        super().__init__(name)
        self.edible = False


class Fruit(Plant):     # Фрукт
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


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
