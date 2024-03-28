def line(dlina, puti, simvol):
    if puti == "бок":
        print(simvol * dlina)
    elif puti == "низ":
        for i in range(dlina):
            print(simvol)


line(15, "низ", "*")
