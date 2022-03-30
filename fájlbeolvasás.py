j=open("nevezetessegek.txt","r")

adatok=[]

for i in j:
    t=i[:-1].split(";")
    adatok.append(t)

print(adatok)

def evszam(lista):
    for i in (0,len(lista)):
        if lista[i][2]==kerdes1:
            print(lista[i][0])
            break
        else:
            print("Nincs ilyen")

def orszagnev(lista):
    for i in (0,len(lista)):
        if lista[i][1]==kerdes2:
            print(lista[i][0])
            break
        else:
            print("Nincs ilyen")

valasztas=int(input("Írj be egy 1-est ha keresni akarsz évszám alapján. Írj be egy 2-est ha keresni akarsz országnév alapján: "))

if valasztas==1:
    kerdes1=input("Adj meg egy évszámot: ")
    evszam(adatok)
elif valasztas==2:
    kerdes2=input("Adj meg egy országnevet: ")
    orszagnev(adatok)

