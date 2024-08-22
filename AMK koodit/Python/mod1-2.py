#teht 1.1
#tulostaa nimen
print("Micael Raste")

#teht 2.1
#kysyy nimen ja tulostaa tervehdyksen
nimi = input("Anna nimesi: ")
print(f"Terve, {nimi}!")

#teht 2.2
#kysyy ympyrän säteen
sade = input("Anna ympyrän säde: ")
#laskee pinta-alan
pintala = 3.14 * float(sade) ** 2
#tulostaa pinta-alan
print("Ympyrän pinta-ala on", pintala)

#teht 2.3
#kysyy suorakulmion kannan ja korkeuden
kanta = input("Anna suorakulmion kanta: ")
korkeus = input("Anna suorakulmion korkeus: ")
#laskee piirin ja pinta-alan
piiri = float(kanta) * 2 + float(korkeus) * 2
suorala = float(kanta) ** float(korkeus)
#tulostaa piirin ja pinta-alan
print("Suorakulmion piiri on", piiri, "ja pinta-ala on", suorala)

#teht 2.4
#funktio summaa ja kertoo luvut listasta
def mul(numlist):
    result = 1
    for i in numlist:
        result *= i
    return result

#lista luvuista
numlist = []
#kysyy 3 lukua ja lisää ne listaan
for i in range(3):
    num = input("Anna luku: ")
    numlist.append(float(num))
#tuostaa summan, tulon ja keskiarvon
print("Lukujen summa on", sum(numlist), "Lukujen tulo on", mul(numlist), "ja keskiarvo on", sum(numlist) / len(numlist))

#teht 2.5
#funktio muuntaa kaikki luodeiksi
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
#lisää random lisukkeen
import random
#funktio tulostaa listan numerot peräkkäin
def printable(list):
    return "".join([str(i) for i in list])
#lisää 3 numeroa randomisti 0-9 väliltä
num1 = [random.randint(0, 9) for i in range(3)]
#lisää 4 numeroa randomisti 1-6 väliltä
num2 = [random.randint(1, 6) for i in range(4)]
#tulostaa molemmat listat
print("Ensimmäinen luku: ", printable(num1), "Toinen luku: ", printable(num2))
