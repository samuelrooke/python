ajettu_matka = float(input("Anna autolla ajettu vuotuinen matka (km): "))

bensiinin_hinta = float(input("Anna bensiinin hinta: "))

dieselin_hinta = float(input("Anna dieselin hinta: "))

bensiini_kulutus = float(input("Anna bensiinin kulutus (l/100km): "))

diesel_kulutus = float(input("Anna dieselin kulutus (l/100km): "))

dieselvero = float(input("Anna dieselin käyttövoimavero, (yleisesti 300-600): "))

bensiini_kulut = (ajettu_matka / 100) * bensiini_kulutus * bensiinin_hinta
diesel_kulut = (ajettu_matka / 100) * diesel_kulutus * dieselin_hinta + dieselvero


print("Bensiiniauto on vuodessa", round(bensiini_kulut, 2), "euroa")
print("Dieselauto on vuodessa", round(diesel_kulut, 2), "euroa") 

if bensiini_kulut < diesel_kulut:
    ero = diesel_kulut - bensiini_kulut
    print("Bensiiniauto on", round(ero, 2), "euroa halvempi.")
else:
    ero = bensiini_kulut - diesel_kulut
    print("Dieselauto on", round(ero, 2), "euroa halvempi.")