class House:
    # Атрибут класса House. Так же является переменной по своей сути
    houses_history = []

    # Метод класса House. Так же является функцией по своей сути
    # (cls, *args, **kwargs) Параметры. Так же являются переменными по своей сути,
    # но включенными в метод (туже функцию) и принимающие значения которые называются
    # позиционными(data в *args) и именованными аргументами (second=25 и third=3.14 в **kwargs)
    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    # Метод класса House включающий в себя параметры, которые включают в себя атрибуты
    def __init__(self, name, number_of_floors):
        self.name = name                            # Параметр = Атрибут, описывающий наименование
        self.number_of_floors = number_of_floors    # Параметр = Атрибут, описывающий номер этажа

    #  для момента когда выбрали этаж
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(f"Этаж:{i}")
        else:
            print("Такого этажа не существует")

    # Возвращает кол-во этажей
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название:{self.name}, кол-во этажей:{self.number_of_floors}'

    # Череда сравнений.
    # Благодаря которым полагаю можно было бы автоматически вносить разного рода изменения
    # на основе результата.
    def __eq__(self, other):
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return isinstance(other, House) and self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return isinstance(other, House) and self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return isinstance(other, House) and self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return isinstance(other, House) and self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        #   return not self.__eq__(other)
        return self.number_of_floors != other.number_of_floors

    # Меняют кол-во этажей
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    # удаление объекта
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


# test
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
