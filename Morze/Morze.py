with open("morzeabc.txt") as Morzeabc:
    abc={}
    abc_vissza={}
    fejlec = Morzeabc.readline().strip()
    for x in Morzeabc:
        split = x.strip().split('\t')
        abc[split[0]]=split[1]
        abc_vissza[split[1]]=split[0]

class Atalakitott:
    def __init__(self,sze, szo):
        self.Szerzo=sze
        self.Idezet=szo

with open("morze.txt") as Szoveg:
    szoveg = [x.strip() for x in Szoveg]


def Morze2Szoveg(sor, szotar):
    szerzo =""
    szoveg=""
    split = sor.split(';')
    temp1 = split[0].split('       ')
    temp2 = split[1].split('       ')
    sze = [x.split('   ')for x in temp1]
    szo = [x.split('   ') for x in temp2]
    sze[len(sze)-1].remove('')
    for x in range(len(sze)):
        for y in range(len(sze[x])):
            szerzo+=szotar[sze[x][y]]
        szerzo+=" "
    for x in range(len(szo)):
        for y in range(len(szo[x])):
            szoveg+=szotar[szo[x][y]]
        szoveg+=" "
    return Atalakitott(szerzo.rstrip(' '),szoveg)

print(f"3. feladat: a Morze abc {len(abc)} db karakter kódját tartalmazza")
karakter = input("4. feladat: kérek egy karaktert: ")

try:
    print(f"\tA karakter kódja: {abc[karakter]}")
except :
    print(f"Nem található a kódtárban ilyen karakter ")
Idezetek = [Morze2Szoveg(x, abc_vissza) for x in szoveg]
print(f"7. feladat: Az első szerző: {Idezetek[0].Szerzo}")
max =0
Idezet = Atalakitott
for x in Idezetek:
    if len(x.Idezet)>max: max = len(x.Idezet)
for x in Idezetek:
    if len(x.Idezet) ==max: 
        Idezet = x
print(f"8. feladat: Leghosszabb idézet szerzője és az idézet: {Idezet.Szerzo.lstrip(' ')}: {Idezet.Idezet}")
print("9. feladat: Arisztotelész idézetei:")
[print(f"\t-{x.Idezet}") for x in Idezetek if x.Szerzo=="ARISZTOTELÉSZ"]
print("10. feladat: forditas.txt")

with open("forditas.txt","w") as Kiiras:
    [Kiiras.write(f"{x.Szerzo}:{x.Idezet}\n") for x in Idezetek]