pituus = float(input("Hypyn pituus: "))

yhteispisteet = 0.0

tuomari = 1
while tuomari <= 5:
    pisteet = float(input(f"Tuomarin {tuomari} pisteet: "))
    yhteispisteet += pisteet
    tuomari += 1

yhteispisteet += 0.9 * pituus

print(f"Yhteispisteet: {yhteispisteet}")


