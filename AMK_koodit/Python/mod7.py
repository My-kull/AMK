#teht 7.1
# Määritellään vuodenajat
vuodenajat = ("talvi", "kevät", "kesä", "syksy")

# Pyydetään käyttäjältä kuukausi
kuukausi = int(input("Anna kuukauden numero: "))

# Määritetään vuodenaika kuukauden perusteella
if kuukausi in [12, 1, 2]:
    vuodenaika = vuodenajat[0]
elif kuukausi in [3, 4, 5]:
    vuodenaika = vuodenajat[1]
elif kuukausi in [6, 7, 8]:
    vuodenaika = vuodenajat[2]
elif kuukausi in [9, 10, 11]:
    vuodenaika = vuodenajat[3]
else:
    vuodenaika = "Virheellinen kuukausi"

# Tulostetaan vuodenaika
print(vuodenaika)


#teht 7.2
# Alustetaan joukko nimien tallentamista varten
nimet = set()

while True:
    # Pyydetään käyttäjältä nimi
    nimi = input("Anna nimi: ")

    # Tyhjä merkkijono lopettaa syötteen
    if nimi == "":
        break

    # Jos nimi on jo aiemmin syötetty, tulostetaan "Aiemmin syötetty nimi"
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")

    # Jos nimeä ei ole vielä syötetty, lisätään se ja tulostetaan "Uusi nimi"
    else:
        nimet.add(nimi)
        print("Uusi nimi")

# Tulostetaan nimet
for nimi in nimet:
    print(nimi)


#teht 7.3
# Alustetaan sanakirja
lentoasemat = {}

while True:
    # Pyydetään käyttäjältä toiminto
    toiminto = input("Haluatko (1) syöttää uuden lentoaseman, (2) hakea lentoaseman tiedot vai (3) lopettaa? ")

    # Uuden lentoaseman syöttäminen
    if toiminto == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema lisätty.")

    # Lentoaseman tietojen haku
    elif toiminto == "2":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoaseman nimi on", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löydy.")

    # Ohjelman lopettaminen
    elif toiminto == "3":
        print("Ohjelman suoritus päättyy.")
        break

    # Virheellinen toiminto
    else:
        print("Virheellinen toiminto. Yritä uudelleen.")
