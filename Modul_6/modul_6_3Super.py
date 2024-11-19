import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += new_z

    def get_cords(self):
        print(f'x: {self._cords[0]}, y: {self._cords[1]}, z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dive_depth = abs(dz) * self.speed / 2
        new_z = self._cords[2] - dive_depth
        self._cords[2] = max(new_z, 0)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal,Bird):
    sound = "Click-click-click"


# Test

db = Duckbill(10)

print("-" * 305)


print(db.live)

print(db.beak)

print("-" * 305)


db.speak()

db.attack()

print("-" * 305)


db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()

print("-" * 305)


db.lay_eggs()
