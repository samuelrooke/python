pizzat = {
    1: {'nimi': 'Bolognese',
        'taytteet': ['jauheliha'],
        'hinta': 9.90},
    2: {'nimi': 'Frutti di Mare', 
        'taytteet': ['ananas', 'katkarapu', 'tonnikala'],
        'hinta': 10.00},
    3: {'nimi': 'Americano',
        'taytteet': ['ananas', 'aurajuusto', 'kinkku'],
        'hinta': 10.00},
    4: {'nimi': 'Opera Special', 
        'taytteet': ['kinkku', 'salami', 'tonnikala'],
        'hinta': 10.00},
    5: {'nimi': 'Mexicana', 
        'taytteet': ['ananas', 'pepperoni', 'chili', 
                     'tacokastike'],
        'hinta': 11.00},
    6: {'nimi': 'Julia', 
        'taytteet': ['ananas', 'aurajuusto', 'katkarapu', 
                     'kinkku'],
        'hinta': 10.00},
    7: {'nimi': 'Empire Special', 
        'taytteet': ['katkarapu', 'kinkku', 'mustapippuri', 
                     'salami', 'sipuli', 'tuplajuusto', 
                     'valkosipuli'],
        'hinta': 12.90},
    8: {'nimi': 'Kummisetä',
        'taytteet': ['herkkusieni', 'katkarapu', 'kinkku', 
                     'valkosipuli'],
        'hinta': 11.00},
    9: {'nimi': 'Chicken Hawaii', 
        'taytteet': ['ananas', 'aurajuusto', 'kana'],
        'hinta': 9.50},
    11: {'nimi': 'Romeo', 
        'taytteet': ['ananas', 'aurajuusto', 'katkarapu', 
                  'salami'],
        'hinta': 10.00},
    12: {'nimi': 'Vegetariana', 
        'taytteet': ['herkkusieni', 'oliivi', 'paprika', 
                  'sipuli', 'tomaatti'],
        'hinta': 10.00},
    13: {'nimi': 'Dillinger', 
        'taytteet': ['jauheliha', 'kinkku', 'salami', 
                  'sipuli'],
        'hinta': 11.50},
    14: {'nimi': 'Papa''s Special',
        'taytteet': ['aurajuusto', 'mustapippuri', 'oliivi', 
                  'paprika', 'salami', 'sipuli'],
        'hinta': 14.00},
    15: {'nimi': 'Quattro Stagioni', 
        'taytteet': ['herkkusieni', 'katkarapu', 'kinkku', 
                  'paprika'],
        'hinta': 13.00},
    16: {'nimi': 'Cambretti', 
        'taytteet': ['tuplajuusto', 'katkarapu', 
                  'valkosipuli'],
        'hinta': 14.50},
    17: {'nimi': 'Pepperoni', 
        'taytteet': ['paprika', 'pepperoni', 'tonnikala'],
        'hinta': 11.50},
    19: {'nimi': 'Spicy Hot Crispy', 
        'taytteet': ['mausteinen naudanliha', 'sipuli', 
                  'tomaatti', 'chili'],
        'hinta': 13.00},
    21: {'nimi': 'Finlandia', 
        'taytteet': ['kana', 'katkarapu', 'kinkku', 
                  'salami', 'tonnikala'],
        'hinta': 14.00},
    23: {'nimi': 'Driver''s Special', 
        'taytteet': ['pekoni', 'pepperoni', 'kinkku', 
                  'salami', 'aurajuusto'],
        'hinta': 14.50},
    26: {'nimi': 'Fantasia', 
        'taytteet': [None, None, None, None],
        'hinta': 12.00}
}

print("Tervetuloa Guido's Pizza Palaceen, mitä haluaisitte?\n")

print('Menu:')
for numero in sorted(pizzat):
    p = pizzat[numero]
    print(f"{numero}: {p['nimi']} - {p['hinta']:.2f}")

kokonaishinta = 0.0
tilaus_rivit = []

while True:
    val = input('\nAnna pizzan numero (0 = lopetus): ')
    if val.strip() == '0':
        break
    
    if not val.strip().isdigit():
        print('\nVirheellinen pizzan numero!')
        continue

    numero = int(val)
    if numero not in pizzat:
        print('\nVirheellinen pizzan numero!')
        continue

    maara_str = input(f'\nPizzan numero {numero} kappalemäärä: ')
    if not maara_str.strip().isdigit():
        print('Kirjoita määrä numerona (esim. 2).')
        continue
    maara = int(maara_str)
    if maara <= 0:
        print('Anna positiivinen määrä.')
        continue
    if maara > 15:
        print('Anna enintään 15 kappaletta.')
        continue

    hinta = pizzat[numero]['hinta']
    rivin_summa = maara * hinta
    kokonaishinta += rivin_summa
    tilaus_rivit.append((numero, maara, rivin_summa))
    print(f'\nVälisumma: {maara} x {hinta:.2f} = {rivin_summa:.2f} euroa')

print('\nKiitos tilauksestanne! Kokonaishintanne on {0:.2f} euroa.'.format(kokonaishinta))