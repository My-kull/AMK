#teht 1.1
# Tulostaa nimen
print("Micael Raste")

#teht 2.1
# Kysyy nimen ja tulostaa tervehdyksen
nimi = input("Anna nimesi: ")
print(f"Terve, {nimi}!")

#teht 2.2
# Kysyy ympyrän säteen
sade = input("Anna ympyrän säde: ")
# Laskee pinta-alan
pintala = 3.14 * float(sade) ** 2
# Tulostaa pinta-alan
print("Ympyrän pinta-ala on", pintala)

#teht 2.3
# Kysyy suorakulmion kannan ja korkeuden
kanta = input("Anna suorakulmion kanta: ")
korkeus = input("Anna suorakulmion korkeus: ")
# Laskee piirin ja pinta-alan
piiri = float(kanta) * 2 + float(korkeus) * 2
suorala = float(kanta) ** float(korkeus)
# Tulostaa piirin ja pinta-alan
print("Suorakulmion piiri on", piiri, "ja pinta-ala on", suorala)

#teht 2.4
# Funktio summaa ja kertoo luvut listasta
def mul(numlist):
    result = 1
    for i in numlist:
        result *= i
    return result

# Lista luvuista
numlist = []
# Kysyy 3 lukua ja lisää ne listaan
for i in range(3):
    num = input("Anna luku: ")
    numlist.append(float(num))
# Tulostaa summan, tulon ja keskiarvon
print("Lukujen summa on", sum(numlist), "Lukujen tulo on", mul(numlist), "ja keskiarvo on", sum(numlist) / len(numlist))

#teht 2.5
# Funktio muuntaa kaikki luodeiksi
def muunna_kilogrammoiksi_ja_grammoiksi(leiviskat, naulat, luodit):
    yhteensa_luodit = leiviskat * 20 * 32
    yhteensa_luodit += naulat * 32
    yhteensa_luodit += luodit

    # Muunna luodit grammoiksi
    grammoina = yhteensa_luodit * 13.3

    # Muunna grammat kiloksi ja grammoiksi
    kilogrammat = int(grammoina // 1000)
    grammat = grammoina % 1000

    return kilogrammat, grammat

# Kysy käyttäjältä syötteet
leiviskat = float(input("Anna leivisköiden määrä: "))
naulat = float(input("Anna naulojen määrä: "))
luodit = float(input("Anna luotien määrä: "))

# Muunna kilogrammoiksi ja grammoiksi
kilot, grammat = muunna_kilogrammoiksi_ja_grammoiksi(leiviskat, naulat, luodit)

# Tulosta tulos
print(f"Vastaava paino on {kilot} kg ja {grammat:.2f} g.")

#teht 2.6
# Lisää random lisukkeen
import random
# Funktio tulostaa listan numerot peräkkäin
def printable(list):
    return "".join([str(i) for i in list])
# Lisää 3 numeroa randomisti 0-9 väliltä
num1 = [random.randint(0, 9) for i in range(3)]
# Lisää 4 numeroa randomisti 1-6 väliltä
num2 = [random.randint(1, 6) for i in range(4)]
# Tulostaa molemmat listat
print("Ensimmäinen luku: ", printable(num1), "Toinen luku: ", printable(num2))
