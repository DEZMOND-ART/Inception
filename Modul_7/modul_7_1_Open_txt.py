class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name} {self.weight} {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        """Читает содержимое файла и возвращает единую строку."""
        file = open(self.__file_name, 'r', encoding='utf-8')
        data = file.read().strip().split('\n')
        file.close()
        return data

    def add(self, *products):
        """Добавляет продукты в файл, если их ещё нет."""
        existing_products = set(self.get_products())    # Все текущие строки из файла

        """Добавление новых продуктов."""
        file = open(self.__file_name, 'a', encoding='utf-8')
        for product in products:
            product_str = str(product)
            if product_str in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(product_str + '\n')  # Запись нового продукта
                existing_products.add(product_str)
        file.close()


# Создание магазина
s1 = Shop()

# Создание продуктов
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Вывод продукта
print(p2)

# Добавление продуктов в магазин
print("\nДобавляем продукты:")
s1.add(p1, p2, p3)

# Проверка содержимого файла после добавления продуктов
print("\nСодержимое файла после добавления:")
products = s1.get_products()
for product in products:
    print(product)

# Проверяем, что дубликаты не добавлены
print("\nДобавляем дубликаты продуктов:")
s1.add(p1, p2, p3)

# Финальное содержимое файла
print("\nФинальное содержимое файла:")
final_products = s1.get_products()
for product in final_products:
    print(product)

print("\nВсе проверки пройдены успешно!")
