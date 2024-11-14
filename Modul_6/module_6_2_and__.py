class Vehicle:  # Транспортное средство
    __COLOR_VARIANTS = ['red', 'yellow', 'green', 'black']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Владелец транспорта (может меняться)
        self.__model = model  # Модель транспорта (название модели изменить нельзя)
        self.__color = color  # Цвет транспорта (не можем изменить самостоятельно)
        self.__engine_power = engine_power  # Мощность двигателя (не можем изменить самостоятельно)

    def __str__(self):
        return f"Модель: {self.__model}, Цвет: {self.__color}, Владелец: {self.owner}"

    def __int__(self):
        return self.__engine_power

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        print(f"Модель авто: {self.get_model()}, Мощность двигателя: {self.get_horsepower()}HP, Цвет авто: {self.get_color()}, Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
            print(f"Цвет успешно изменен на {new_color}")
        else:
            print(f"Нельзя сменить цвет на {new_color}, доступные цвета: {self.__COLOR_VARIANTS}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['red', 'yellow', 'green', 'black']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
print("-" * 305)

# Изначальные свойства

vehicle1.print_info()
print("-" * 305)

# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'
print("-" * 305)

# Проверяем что поменялось

vehicle1.print_info()
