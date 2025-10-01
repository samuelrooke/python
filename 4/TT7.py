komento = input('> ').strip()

while komento != 'lopeta':
    sanat = komento.split()

    if len(sanat) == 2:
        verbi = sanat[0]
        objekti = sanat[1]
        print(f"ok, komentosi oli siis verbi '{verbi}', objekti = '{objekti}'")

    elif len(sanat) == 1:
        print(f"ok, yksittäinen komento: '{sanat[0]}'")

    elif len(sanat) == 0:
        pass  # tyhjä syöte, ei tehdä mitään

    else:
        print('Anteeksi, en ymmärtänyt komentoa.')

    komento = input('> ').strip()

print('Ohjelma lopetettu.')
