def proizvedenie_elem(spisok):
    otvet = 1
    for i in spisok:
        otvet *= i
    return otvet


spisok = 1, 4, 3, 7, 3234
print(proizvedenie_elem(spisok))
