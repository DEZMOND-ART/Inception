import threading
import time
import random
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        eating_time = random.randint(3, 10)
        time.sleep(eating_time)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = self.find_free_table()
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def find_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(-а)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f'{next_guest.name} Вышел(-шла) из очереди и сел(-а) за стол номер {table.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [

'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',

'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'

]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
