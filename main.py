def chisla(nachalo, konez):
    suma = 0
    for i in range(nachalo, konez + 1):
        suma += i
    return suma


nachalo = 3
konez = 7
print(chisla(nachalo, konez))
