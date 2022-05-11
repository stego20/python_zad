liczba = 1264460
rzad = 1
def towarzysace(lizcba, rzad):
    q = 1
    for i in range(2, lizcba // 2 + 1):
        if lizcba % i == 0:
            q += i
    while rzad < 29:

        if q == liczba:
            return rzad
        else:
            rzad += 1
            return towarzysace(q, rzad)
    return "nit"
print(towarzysace(liczba, rzad))