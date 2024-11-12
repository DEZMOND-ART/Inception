import hashlib
import time


class User:
    # для занесения введенных данных в программу (Хранилище аккаунтов пользователей)
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self._hash_password(password)
        self.age = age

    def _hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)
        # hashlib.sha256 функция для вычисления хеш-значений данных.
        # метод .encode() преобразует обычные строки в байтовые.
        # метод.hexdigest() возвращает хеш в виде шестнадцатеричной строки.

    def check_password(self, password):
        return self.password == self._hash_password(password)
    # проверяет, соответствует ли переданный пароль (после хэширования) сохраненному хэшу.

    def __str__(self):
        return self.nickname
        # выводит только ник


class Video:
    # для занесения введенных данных в программу (хранилище видео)
    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # название
        self.duration = duration    # продолжительность
        self.time_now = 0   # текущее время
        self.adult_mode = adult_mode    # 18+

    def __str__(self):
        return self.title
        # выводит название видео

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()
        # Сравнивает два видео по названию, не учитывая регистр


# Регистрация и вход в программу
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                print(f"Пользователь {nickname} вошел")
            else:
                print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел")

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено")
            else:
                print(f"Видео '{video.title}' уже существует")

    def get_videos(self, search):
        search = search.lower()
        result = [video.title for video in self.videos if search in video.title.lower()]
        return result

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print(f"Видео '{title}' не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(video.time_now + 1, video.duration + 1):
            print(second, end=' ', flush=True)
            time.sleep(1)
        video.time_now = 0
        print("Конец видео")

    def __str__(self):
        return f"UrTube (Текущий пользователь: {self.current_user})"


# Тестовый код для проверки работы классов

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 10)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')