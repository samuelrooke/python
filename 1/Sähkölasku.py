kulutus = float(input('Anna sähkönkulutus (kWh): '))
perusmaksu = 1.79
energiamaksu = 6.29
siirtohinta = 3.98
vero = 2.79372
f = (kulutus * energiamaksu / 100) + perusmaksu + (kulutus * siirtohinta / 100)
yhteensa = f + (f * vero / 100)
print ('Sähkölaskusi on:', round(yhteensa, 2), 'euroa')