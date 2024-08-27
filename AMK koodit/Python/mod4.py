#teht 4.1
temp = 0
# Looppi tulostaa kaikki kolmella jaolliset luvut tuhanteen asti
while temp <= 1000:
    if temp % 3 == 0:
        print(temp)
        temp= temp + 1
    else:
        temp= temp + 1

#teht 4.2
# Looppi muuntaa tuumamäärän senteiksi
while True:
    # Kysyy tuumamäärän
    temp = float(input("Anna tuumamäärä: "))
    # Jos tuumamäärä on negatiivinen, lopetetaan
    if temp < 0:
        break
    # Tulostaa tuumamäärän sentteinä
    print(f"Sentteinä: {temp*2.54}")

#teht 4.3
temp = []
while True:
    # Kysyy luvun
    num = input("Anna luku: ")
    # Jos luku on tyhjä, lopetetaan
    if num == "":
        break
    # Lisää luvun listaan
    temp.append(float(num))
# Tulostaa listan suurimman ja pienimmän luvun
print(f"Suurin luku on {max(temp)} ja pienin luku on {min(temp)}")

#teht 4.4
# Lisätään random-moduuli
import random
answer = random.randint(1, 10)
while True:
    # Kysyy arvausta
    guess = int(input("Arvaa luku väliltä 1-10: "))
    # Jos arvaus on oikein, lopetetaan
    if guess == answer:
        print("Oikein!")
        break
    # Jos arvaus on liian pieni
    elif guess < answer:
        print("Liian pieni arvaus!")
    # Jos arvaus on liian suuri
    else:
        print("Liian suuri arvaus!")

#teht 4.5
user = "python"
password = "rules"
retries = 0
while retries < 5:
    # Kysyy käyttäjänimen ja salasanan
    username = input("Anna käyttäjänimi: ")
    passw = input("Anna salasana: ")
    # Jos käyttäjänimi ja salasana ovat oikein, lopetetaan
    if username == user and passw == password:
        print("Tervetuloa!")
        break
    # Jos käyttäjänimi tai salasana on väärin, kysyy ne uudelleen ja lisää yhden yrityksen
    else:
        print("Pääsy evätty!")
        retries += 1

#teht 4.6
# Kysyy pistemäärän
dots = int(input("Anna pistemäärä: "))
temp = 0
# Pisteiden määrä ympyrän sisällä
inside = 0
# Looppi generoi satunnaisia pisteitä ja tarkistaa ovatko ne ympyrän sisällä
while temp <= dots:
    # Generoi satunnaiset x- ja y-koordinaatit
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # Tarkista onko piste ympyrän sisällä
    if x**2 + y**2 <= 1:
        inside += 1
    temp += 1
# Laske piin likiarvo
pi_approx = 4 * inside / dots
# Tulosta piin likiarvo
print(f"Piin likiarvo on {pi_approx}")
