class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = int(health_points)
        self.catchphrase = catchphrase

    def say_hero_name(self):
        print(f"hero name : {self.name}")

    def double_health(self):
        self.health_points **= 2
        return

    def __str__(self):
        return f'nickname : {self.nickname}, superpower : {self.superpower}, health : {self.health_points}'


class Air_heroes(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, bending, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.bending = bending
        self.fly = fly
        self.damage = damage

    def double_health(self):
        self.health_points **= 2
        self.fly = True
        return f'health points squared: {self.health_points}\nfly = {self.fly}'

    def say_information(self):
        return "True in the " + self.catchphrase


class Earth_heroes(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, bending, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.bending = bending
        self.fly = fly
        self.damage = damage

    def double_health(self):
        self.health_points **= 2
        self.fly = True
        return f'health points squared: {self.health_points}\nfly = {self.fly}'

    def say_information(self):
        return "True in the " + self.catchphrase

class Villain(Air_heroes):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, bending, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, bending, damage, fly)


    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2
        return self.damage



piter = SuperHero('Peter', 'Spider-Man', 'Strength', 300, "I'm your friendly neighbor")
piter.say_hero_name()
piter.double_health()
print(piter)

aang = Air_heroes('Aang', 'Avatar', 'Air Bending', 50, '...', 'Air', 30)
print(aang.double_health())
print(aang.fly)
print(aang.say_information())

tof = Earth_heroes('Tof', 'Blind Bandit', 'Earth Bending', 60, '...', 'Earth', 50)
print(tof.double_health())
print(tof.fly)
print(tof.say_information())

spirit = Villain('Hey Bye', 'Forest Spirit', 'Unknown', 30, '..', 'Spirit', 60)
print(spirit.crit())

aang_villain = Villain('Aang', 'Avatar', 'Air Bending', 50, '...', 'Air', 40)
print(aang_villain.crit())
