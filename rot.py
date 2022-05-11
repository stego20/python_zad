print( 'zad 1')
tekst="LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA"
tekstpop=''
for i in range(len(tekst)):
    if tekst[i]!=' ':
        if ord(tekst[i])+13>90:
            ile=((ord(tekst[i])+13)-90)+65
        else:
            ile=ord(tekst[i])+13
        tekstpop+=chr(ile)
    else:
        tekstpop+=' '
print(tekstpop)
# print(ord("A"))
# print(chr(65))

print('\n')
print( 'zad 2')
tekst2="LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA"
litery=[]
pamiec=[' ']
ile_spacji=tekst2.count(' ')
ilemax=len(tekst2)-ile_spacji
for i in tekst2:
    if i not in pamiec:
        ile2=tekst2.count(i)
        procent=round((ile2/ilemax)*100,1)
        litera_i_procent=[i,procent]
        litery.append(litera_i_procent)
        pamiec.append(i)
litery.sort()
for i in litery:
    if i[1]>5.0:
        print(i[0]," : ",i[1])