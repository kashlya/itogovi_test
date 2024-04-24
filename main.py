def task_1(a, b):
    c = a * a + b * b
    print(f"задание 1: {round(c ** 0.5, 2)}")


b = int(input("b= "))
a = int(input("a= "))
task_1(a, b)


def task_2(a, b):
    c = []
    for i in a:
        for s in b:
            if i == s:
                if i not in c:
                    c.append(i)
                    break
    return c


a = [1, 2, 3, 4]
b = [3, 4, 7, 90]
p = task_2(a, b)
print(f"задание 2: {p}")


def task_3(a):
    num_spisok = []
    num_kortej = []

    for i in a.split(','):
        num_spisok.append(int(i))

    for i in a.split(','):
        num_kortej.append(int(i))

    num_kortej = tuple(num_kortej)

    return num_spisok, num_kortej


a = input(": ")
spisok, kortej = task_3(a)

print(f"задание 3: {"Список:", spisok}")
print(f"задание 3: {"Кортеж:", kortej}")


def task_4(a, b):
    num = []
    for i in a:
        if i not in b:
            num.append(i)
    return num


a = input(": ")
b = input(": ")
otvet = task_4(a, b)
print(f"задание 4: {otvet}")


def task_5(a):
    num = set()
    for i in a:
        if i in num:
            return False
        num.add(i)
    return True


a = input(": ").split()
if task_5(a):
    print(f"задание 5:{"unikalnie"}")
else:
    print(f"задание 5: {"ne unikalnie"}")


def task_6(rik):
    if (rik % 4 == 0 and rik % 100 != 0) or (rik % 400 == 0):
        return True
    else:
        return False


rik = int(input(": "))
if task_6(rik):
    print(f"задание 6: {"visokosnii"}")
else:
    print(f"задание 6: {"obichnii"}")


def task_7(a):
    num = str(a)
    tochka = num.find(".")
    num1 = num[tochka + 1]
    return num1


a = float(input(": "))
print(f"задание 7: {task_7(a)}")


def task_8(a):
    slovo1, slovo2 = a.split()
    otvet = f"{slovo2} {slovo1}"
    return otvet


a = input(": ")
print(f"задание 8: {task_8(a)}")


def task_9(a):
    v1 = a.find("f")
    if v1 == -1:
        return -1
    v2 = a.find("f", v1 + 1)
    if v2 == -1:
        return -2
    return v2


a = input(": ").lower()
print(f"задание 9: {task_9(a)}")


def task_10(*a):
    bolshie = 0
    proshloe_ch = a[0]
    for i in a[1:]:
        if i > proshloe_ch:
            bolshie += 1
        proshloe_ch = i
    return bolshie


a = 0, 1, 2, 3, 4, 5
print(f"задание 10: {task_10(*a)}")
