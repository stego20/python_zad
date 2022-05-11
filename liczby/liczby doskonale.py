liczba=28
def doskonala(liczba):
    suma=0
    for i in range(1,liczba):
        if liczba%i==0:
            suma+=i
    return suma

if liczba==doskonala(liczba):
    print('liczba doskonala')
else:
    print('liczba nie doskonala')