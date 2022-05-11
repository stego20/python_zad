def funkcjaf(liczba):
    suma=0
    for i in liczba:
        suma+=int(i)
    return suma
def funkcjag(liczba, liczba2):
    suma=liczba2*liczba2+liczba
    return suma

podane=[2,1,30,42,2,731]
# podane=[78,1806,4997888322]
wyjscieliczb=[1]
# liczba=2019
liczba=1
while 0<1:
    liczbastr=str(liczba)
    funkcjafwynik=funkcjaf(liczbastr)
    liczba=funkcjag(liczba,funkcjafwynik)
    wyjscieliczb.append(liczba)
    if liczba>max(podane):
        break

for i in podane:
    if wyjscieliczb.count(i)>=1:
        print(i,"    TAK")
    else:
        print(i,"    NIE")

