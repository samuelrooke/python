def muunna(asteet, mista, mihin):
    if mista not in ['c', 'f', 'k'] or mihin not in ['c', 'f', 'k']:
        return None
    
    if mista == mihin:
        return asteet
    
    if mista == "c" and mihin == "f":
        result = (asteet * 9/5) + 32
    elif mista == "f" and mihin == "c":
        result = (asteet - 32) * 5/9
    elif mista == "c" and mihin == "k":
        result = asteet + 273.15
    elif mista == "k" and mihin == "c":
        result = asteet - 273.15
    elif mista == "f" and mihin == "k":
        result = (asteet - 32) * 5/9 + 273.15
    elif mista == "k" and mihin == "f":
        result = (asteet - 273.15) * 9/5 + 32
    
    return round(result, 1)

while True:
    try:
        lampotila = float(input("Anna lämpötila: "))
        break
    except ValueError:
        print("Anna lämpötila numerona...")

mista = input("Mistä asteikosta (c/f/k): ").lower()
mihin = input("Mihin asteikkoon (c/f/k): ").lower()

tulos = muunna(lampotila, mista, mihin)

if tulos is None:
    print("Käytä vain kirjaimia c, f tai k")
else:
    asteikot = {'c': 'Celsius', 'f': 'Fahrenheit', 'k': 'Kelvin'}
    print(f"{lampotila} {asteikot[mista]} = {tulos} {asteikot[mihin]}")