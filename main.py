from random import choice


class Enigma:
    def __init__(self, odin, dva, tri, chetiri):
        self.odin = odin
        self.dva = dva
        self.tri = tri
        self.chetiri = chetiri
        self.shifr = self.random_chisla()

    def __str__(self):
        return str(self.shifr)

    def random_chisla(self):
        znaki = choice(["+", "-", "*", "/"])
        if znaki == "+":
            return self.odin + self.dva + self.tri + self.chetiri
        if znaki == "-":
            return self.odin - self.dva - self.tri - self.chetiri
        if znaki == "*":
            return self.odin * self.dva * self.tri * self.chetiri
        if znaki == "/":
            return self.odin / self.dva / self.tri / self.chetiri


otvet = Enigma(4, 2, 5, 8)
print(otvet.shifr)
