from random import randint


class Student:

    def __init__(self, name):
        self.name = name
        self.study = 10
        self.cash = 100
        self.fatigue = 10
        self.happy = 10
        self.thump = 0.1
        self.alive = True

    def to_study(self):
        print("Время учиться...")
        self.cash -= 5
        self.fatigue -= 0.25
        self.happy -= 0.25
        self.thump -= 1
        self.study += 5

    def to_work(self):
        print("Время заработать...")
        self.cash += 15
        self.fatigue -= 0.25
        self.happy -= 0.25
        self.thump -= 1
        self.study -= 0.5

    def to_rest(self):
        print("Время отдыхать...")
        self.cash -= 5
        self.fatigue += 0.5
        self.happy += 0.5
        self.thump -= 1
        self.study -= 0.5

    def to_fun(self):
        print("Время веселится...")
        self.cash -= 10
        self.fatigue -= 0.25
        self.happy += 1.5
        self.thump += 1
        self.study -= 0.5

    def to_sleep(self):
        print("Время бухать!!")
        self.cash -= 5
        self.fatigue += 2
        self.happy += 1.5
        self.thump -= 1
        self.study -= 0.5

    def is_alive(self):
        if self.cash < 0:
            print("Все деньги закончились...")
            self.alive = False
        elif self.fatigue < 0:
            print("Вы переутомились...")
            self.alive = False
        elif self.thump > 5:
            print("Алкогольная кома):")
            self.alive = False
        elif self.study < 0:
            print("Очислен")
            self.alive = False
        if self.cash <= 15:
            self.to_work()
            print("деньги почти закончились!")
        if self.study <= 5:
            self.to_study()
            print("учись, тебе угрожает очисление!!")
        if self.happy <= 3:
            self.thump += 2
            print("похоже у вас сильная депрессия")

    def end_of_day(self):
        print(f"оценка {round(self.study)}\nденьги {round(self.cash)}")

    def live(self, day):
        print(f"день {day} имя {self.name}")
        live_cube = randint(1, 5)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_work()
        elif live_cube == 4:
            self.to_fun()
        elif live_cube == 5:
            self.to_rest()
        self.end_of_day()
        self.is_alive()


dima = Student(name="Дима")
for day in range(1, 366):
    if dima.alive == False:
        break
    dima.live(day)
