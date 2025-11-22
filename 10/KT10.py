import json
from paikat import Paikka

def main():
    paikat = []

    with open(r"C:\Users\srook\OneDrive - TUNI.fi\Työpöytä\Koulu\python\10\paikat.json", "r", encoding="utf-8") as f:


        data = json.load(f)

    for item in data:
        paikka = Paikka(item["nimi"], item["kuvaus"])
        paikat.append(paikka)
    for p in paikat:
        print(p)

if __name__ == "__main__":
    main()
