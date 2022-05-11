liczby_nieparzyste=[]
pamiec=[]
pamiec2=[]
#tworze liste liczb od 1 do 10000 i dodaje liczby tylko nieparzyste
for i in range(1,10001,2):
    liczby_nieparzyste.append(i)
index=1
#tworze nie skonczona pentla
while 1>0:

    liczba=0
    coile=liczby_nieparzyste[index]
    #sprawdzam pokolei wszystkie liczby
    for i in range(0,len(liczby_nieparzyste)):
        liczba+=1
        if liczba%coile!=0:
            pamiec.append(liczby_nieparzyste[i])
    liczby_nieparzyste = pamiec
    #sprawddza czy poprzedni układ liczb jest taki sam jak aktualny układ liczb jeżeli tak to pentla sie konczy i wyświetla się wynik
    if pamiec2==pamiec:
        break
    pamiec = []
    pamiec2=liczby_nieparzyste
    index+=1
print(liczby_nieparzyste)