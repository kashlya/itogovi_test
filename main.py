def prostoe_li_chislo(chislo):
    if chislo % 2 == 0:
        return "false"
    if chislo <= 1:
        return "false"
    if chislo == 2:
        return "true"
    for i in range(3, int(chislo ** 0.5) + 1, 2):
        if chislo % i == 0:
            return False
    return True


print(prostoe_li_chislo(41))
