import math


class Figure:
    sides_count = 0     # количество сторон, уникальное для каждой фигуры

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]  # устанавливает цвет по умолчанию
        self.filled = False
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count  # устанавливает массив сторон по умолчанию

    def __is_valid_color(self, r, g, b):    # проверяет что переданы 3 целых числа
        return all(isinstance(colors, int) and 0 <= colors <= 255 for colors in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):    # извлекает значение инкапсулированного атрибута __color
        return self.__color

    def __is_valid_sides(self, *sides):     # проверяет кол-во сторон
        return (len(sides) == self.sides_count and  # проверяет, являются ли стороны положительными целыми числами
                all(isinstance(side, int) and side > 0 for side in sides))

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):    # извлекает значение инкапсулированного атрибута __sides
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = len(self) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side = sides[0] if sides and isinstance(sides[0], int) and sides[0] > 0 else 1
        super().__init__(color, *(side for _ in range(self.sides_count)))

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


# Test
circle1 = Circle((200, 200, 100), 10)  # Цвет, длина окружности
cube1 = Cube((222, 35, 130), 6)  # Цвет, сторона куба

# Изменяется ли цвет
circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (длины окружности)
print(len(circle1))

# Проверка объёма куба
print(cube1.get_volume())
