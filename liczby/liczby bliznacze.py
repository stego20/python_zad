liczba1=11
liczba2=13
def pierwsza(liczba):
    for i in range(2,liczba):
        if liczba%i==0:
            return False
    return True
# print(pierwsza(liczba2))
if pierwsza(liczba1)==True and pierwsza(liczba2)==True :
    if liczba1-liczba2==2 or liczba2 -liczba1==2:
        print('liczby bliżnacze')
    else:
        print('liczby nie bliżnacze')
else:
    print('liczby nie bliżnacze')