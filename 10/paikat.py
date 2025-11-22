class Paikka:
    def __init__(self, nimi, kuvaus):
        self.nimi = nimi
        self.kuvaus = kuvaus

    def __str__(self):
        return f"{self.nimi}: {self.kuvaus}"
