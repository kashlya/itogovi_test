def lucky_chislo(chislo):
    b = []
    while chislo > 0:
        b.append(chislo % 10)
        chislo = chislo // 10
    b = b[::-1]
    if b[0] + b[1] + b[2] == b[3] + b[4] + b[5]:
        print("true")
    else:
        print("false")


lucky_chislo(612711)
