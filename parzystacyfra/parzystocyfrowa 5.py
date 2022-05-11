liczba=7921
parzytsa=0
parzytsacyfra=[]
z=-1
while len(parzytsacyfra) - 1 < liczba:
    #wykonujemy pentle dopuki długość listy nie będzie większa od liczby o 1
    z+=1
    z = str(z)
    for i in z:
        # dzielimy lizcba na pojedyńcze znaki i sprawdzamy czy ta liczba jest parzysta np. liczbe 157 rozdzielamy na 1 , 5, 7
        i = int(i)
        if i % 2 == 0:
            # jeżeli znak jest parzysty to dodajemy +1 do argumentu parzytsa
            parzytsa += 1
    if parzytsa == len(z):
        # jeżeli argument parzytsa jest równy długości liczby to dodajemy do listy parzytsacyfra
        parzytsacyfra.append(z)

        parzytsa = 0
    # elif len(parzytsacyfra) - 1 > liczba:
    #     break
    else:
        parzytsa = 0
    z=int(z)
print(parzytsacyfra[liczba])