class Pizza:
    def __init__(self, nimi, taytteet):
        self.nimi = nimi

        self.taytteet = list(taytteet)

        self.hinnat = (0.0, 0.0, 0.0)

    def hae_taytteet(self):
        return ", ".join(self.taytteet)

    def onko_tayte(self, t):
        return t in self.taytteet

    def aseta_hinnat(self, normaali_hinta, perhe_hinta, pannu_hinta):
        self.hinnat = (float(normaali_hinta), float(perhe_hinta), float(pannu_hinta))

    def hae_hinnat(self):
        return self.hinnat


if __name__ == '__main__':
    pizzat = {
        1: Pizza('Margherita', ['mozzarella', 'tomaatti']),
        2: Pizza('Bolognese', ['jauhelihakastike']),
        3: Pizza('Americana', ['kinkku', 'ananas', 'aurajuusto']),
        4: Pizza('Julia', ['ananas', 'aurajuusto', 'katkarapu', 'kinkku']),
        5: Pizza('Kummisetä',['herkkusieni', 'katkarapu', 'kinkku', 'valkosipuli'])
    }

    pizzat[1].aseta_hinnat(10.5, 18, 15)
    pizzat[2].aseta_hinnat(11, 18 ,15)
    pizzat[3].aseta_hinnat(11, 20 ,16)
    pizzat[4].aseta_hinnat(10, 14 ,13)
    pizzat[5].aseta_hinnat(11, 16 ,15)

    print()
    print('Nro  Nimi                      Normaali   Perhe   Pannu')

    for nro, p in sorted(pizzat.items()):
        normaali, perhe, pannu = p.hae_hinnat()
        nimi = p.nimi
        taytteet = p.hae_taytteet()
        
        # Sisennys
        print(f"{nro:2d} {nimi:25s} {normaali:8.2f} {perhe:8.2f} {pannu:8.2f}")
        print(f"    {taytteet}\n")