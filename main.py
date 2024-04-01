def prostie_chisla(chislo):
    if chislo <= 1:
        return False
    if chislo == 2:
        return True
    if chislo % 2 == 0:
        return False
    for i in range(3, int(chislo ** 0.5) + 1, 2):
        if chislo % i == 0:
            return False
    return True


spisok = [7, 17, 13, 19, 4, 8]
prostie = 0
for s in spisok:
    if prostie_chisla(s):
        prostie += 1
print(prostie)
