# KT 5 Lämpötilamuunnos

## Tee Python-funktio, joka muuntaa lämpötiloja eri asteikkojen välillä: Celsius, Fahrenheit ja Kelvin. Sitten käytä funktiota Python-ohjelmassa, joka kysyy käyttäjältä lämpötilan sekä tiedon siitä missä asteikossa se on, ja mihin asteikkoon se muunnetaan. Ohjelmalla pitäisi siis esimerkiksi voida muuntaa Celsius-asteikossa annettu lämpötila Fahrenheit-asteikolle.

### Funktiolla pitäisi olla kolme parametria

### ·       asteet – lämpötila asteina

### ·       mista – merkkijono ’f’, ’k’ tai ’c’ riippuen siitä onko kyseessä Fahrenheit-, Kelvin- vai Celsius-asteikko

### ·       mihin – samanlainen kuin mista-parametri

Funktion pitää palauttaa lämpötila joka on annettu mistä-asteikossa muunnettuna mihin-asteikkoon.

Funktion käyttöesimerkki (olettaen, että funktion nimeksi on annettu muunna):

lampotila = 99.9
tulos = muunna(lampotila, 'f', 'c')

print(f'{lampotila} astetta Fahrenheitia on {tulos} astetta Celsiusta.')

Edellinen esimerkki tulostaisi:

99.9 astetta Fahrenheitia on 37.7 astetta Celsiusta.

Voit halutessasi pyöristää lopputuloksen esimerkiksi yhteen desimaaliin round-funktiolla.

Vinkki: voit hyödyntää funktiossa esimerkiksi sisäkkäisiä if-käskyjä, joissa tutkitaan mista- ja mihin-parametrien arvoja. Mieti myös virhetilanteiden käsittelyä: mitä tapahtuu jos joku välittää funktiolle jotain muita kuin c, f tai k? Entä jos mistä ja mihin ovat samat?

Toinen vinkki: voit ensin tehdä ohjelman, joka tekee muunnokset, ja sitten siirtää olennaisen osan ohjelmasta funktioksi.

Tarvittavat laskukaavat löydät esimerkiksi täältä: Temperature Conversion Formulas