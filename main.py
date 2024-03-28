def chisla(pervoe, vtoroe, tretie, chetvertoe):
    max_ch = pervoe
    if vtoroe > max_ch:
        max_ch = vtoroe
    if tretie > max_ch:
        max_ch = tretie
    if chetvertoe > max_ch:
        max_ch = chetvertoe
    return max_ch


print(chisla(1, 5, 3, 2))
