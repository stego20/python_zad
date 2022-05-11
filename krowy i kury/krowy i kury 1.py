glowy=4
nogi=10
pamiec_glowy=glowy
krowy=0
kury=0
while glowy>0 or nogi>0:
    if int(glowy / 2)*4+int(glowy/2)*2==nogi and glowy==pamiec_glowy :
        krowy =kury= glowy / 2
        glowy=0
        break
    elif int(glowy / 4) == glowy or int(glowy / 2) == glowy and glowy==pamiec_glowy:
        if nogi % glowy == 0:
            if nogi % 2 == 0 and nogi / 2 == glowy:
                kury = y / 2
            elif nogi % 4 == 0 and nogi / 4 == glowy:
                krowy = nogi / 4
        glowy = 0
        break

    elif nogi-4>=0 and glowy-1>=0:
        nogi-=4
        glowy-=1
        krowy+=1
    elif nogi-2>=0 and glowy-1>=0:
        nogi-=2
        glowy-=1
        kury+=1
    else:
        while glowy>0:
            if glowy>0:
                krowy-=1
                kury+=2
                glowy-=1
        break

print('krowy: ',int(krowy),"     kury: ",int(kury))