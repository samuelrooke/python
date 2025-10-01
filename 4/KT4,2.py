pituus = float(input("Hypyn pituus: "))

yhteispisteet = 0.0

for tuomari in range(1, 6):
    pisteet = float(input(f"Tuomarin {tuomari} pisteet: "))
    yhteispisteet += pisteet

yhteispisteet += 0.9 * pituus

print(f"Yhteispisteet: {yhteispisteet}")

