tiedosto = open("kysymykset.txt", "r", encoding="utf-8")
rivit = tiedosto.readlines()
tiedosto.close()

kysymykset = []
vaihtoehtoja = 0
i = 0

while i < len(rivit):
    rivi = rivit[i].strip()
    
    if rivi == "":
        i = i + 1
        continue
    
    kysymys = rivi
    i = i + 1
    
    vastaukset = []
    while i < len(rivit) and len(rivit[i].strip()) > 1:
        vastaukset.append(rivit[i].strip())
        i = i + 1
    
    if vaihtoehtoja == 0:
        vaihtoehtoja = len(vastaukset)
    if len(vastaukset) != vaihtoehtoja:
        print("Virhe tiedostossa!")
        exit()
    
    oikea = rivit[i].strip()
    i = i + 1
    
    kysymykset.append([kysymys, vastaukset, oikea])

pisteet = 0

for numero in range(len(kysymykset)):
    k = kysymykset[numero]
    
    print()
    print("Kysymys", numero + 1, ":", k[0])
    for i, v in enumerate (k[1]):
        print (f"{chr(97 + i)}) {v}")

    while True:
        v = input("Vastauksesi: ")
        if v == "a" or v == "b" or v == "c":
            break
        else:
            print("Valitse a, b tai c!")
    
    if v == k[2]:
        print("Oikein!")
        pisteet = pisteet + 1
    else:
        print("Väärin!")

print()
print("Sait", pisteet, "/", len(kysymykset), "oikein.")