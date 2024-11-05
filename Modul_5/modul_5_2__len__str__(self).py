class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
            if 1 <= new_floor <= self.number_of_floors:
                for i in range(1, new_floor + 1):
                    print(f"Этаж:{i}")
            else:
                print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название:{self.name}, кол-во этажей:{self.number_of_floors}'


# test
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# с 1 до выбранного этажа включительно
h1.go_to(5)
h2.go_to(10)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
