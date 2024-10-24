from time import sleep
from urllib.request import install_opener
from venv import create

from geopy import distance
import random
import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="aroundtheworld",
    user="ympari",
    password="1234",
    collation="utf8mb4_general_ci",
    autocommit=True,
)


# muokattu pelinluontiskripti, pitkälti lainattu esimerkkipelistä
def create_game(start_money, cur_airport, tired):
    sql = "INSERT INTO game (money, location, tired) VALUES (%s, %s, %s);"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (start_money, cur_airport, tired))
    g_id = cursor.lastrowid
    return g_id


# haetaan nykyisen kentän pituuspiiri
def get_current_longitude():
    sql = f"SELECT longitude_deg FROM airport WHERE ident = %s;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (current_ap,))
    result = cursor.fetchone()
    return result.get("longitude_deg") if result else None


# kopioitiin esimerkistä lentokentän tarvittavan tiedon haku sekä etäisyyksien lasku
def get_airport_info(icao):
    sql = f"""SELECT iso_country, ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


def calculate_distance(current, target):
    start = get_airport_info(current)
    end = get_airport_info(target)
    if start and end:
        return distance.distance(
            (start.get("latitude_deg"), start.get("longitude_deg")),
            (end.get("latitude_deg"), end.get("longitude_deg")),
        ).km
    return None


# haetaan lähimmät 9 lentokenttää, sekä asetetaan niille järjestysnumerot 1-9
# jos kenttiä on vähemmän kuin 9, niin funktio palauttaa niin monta kenttää kuin mahdollista
def get_easterner_ap(c_ap):
    nineclosest = {}
    listnine = []

    sql = f"SELECT name, longitude_deg, latitude_deg, ident FROM airport WHERE longitude_deg > '{get_current_longitude()}' ORDER BY longitude_deg;"
    cursor = connection.cursor(dictionary=True, buffered=True)
    cursor.execute(sql)
    ran = len(cursor.fetchall())
    cursor.execute(sql)
    for i in range(ran):
        result = cursor.fetchone()
        if result and 300 < calculate_distance(c_ap, result.get("ident")):
            tuple = (
                calculate_distance(c_ap, result.get("ident")),
                result.get("name"),
                result.get("ident"),
            )
            listnine.append(tuple)
    sortedlist9 = sorted(listnine)
    a = 0
    for i in range(len(sortedlist9) - 1):
        if a < 9:
            a += 1
            nineclosest.update({a: sortedlist9[a]})
    return nineclosest


# sama kuin edeltävä funktio, mutta palauttaa kaikki idämpänä olevat kentät
def checkforgoal(c_ap):
    listnine = []
    dictlist9 = {}
    sql = f"SELECT name, longitude_deg, latitude_deg, ident FROM airport WHERE longitude_deg > '{get_current_longitude()}' ORDER BY longitude_deg;"
    cursor = connection.cursor(dictionary=True, buffered=True)
    cursor.execute(sql)
    ran = len(cursor.fetchall())
    cursor.execute(sql)
    for i in range(ran):
        result = cursor.fetchone()
        if result and 300 < calculate_distance(c_ap, result.get("ident")):
            tuple = (
                calculate_distance(c_ap, result.get("ident")),
                result.get("name"),
                result.get("ident"),
            )
            listnine.append(tuple)
    sortedlist9 = sorted(listnine)
    a = 0
    for i in range(len(sortedlist9) - 1):
        a += 1
        dictlist9.update({a: sortedlist9[a]})
    return dictlist9


# päivitetään pelaajan sijainti tietokantaan. funktio pitkälti kopioitu esimerkistä, muutettu arvot vastaamaan pelin tarvitsemia arvoja
def update_location(icao, p_tired, u_money, g_id):
    sql = f"""UPDATE game SET location = %s, tired = %s, money = %s WHERE id = %s"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao, p_tired, u_money, g_id))


def record_highscore(distance, co2, timespent, game_id):
    sql = f"""INSERT INTO highscores (DistanceTravelled, co2Consumed , DaysTravelled, g_id) VALUES (%s, %s, %s, %s);"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (distance, co2, timespent, game_id))


def fetch_highscores():
    list = []
    sql = f"SELECT DistanceTravelled, co2Consumed, DaysTravelled FROM highscores order by g_id DESC limit 10;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    ran = len(cursor.fetchall())
    cursor.execute(sql)
    for i in range(ran):
        result = cursor.fetchone()
        list.append(result)
    return list


def read_highscores():
    ask = input(f"Haluatko nähdä 10 viimeisintä tulosta? (Y/N): ")
    if ask.upper() == "Y":
        list = fetch_highscores()
        for i in range(len(list)):
            print(list[i])
        input("Paina enter jatkaaksesi")
        return
    else:
        input("Paina enter jatkaaksesi")
        return


def story(c_ap, notover):
    if c_ap == "EGGW" and notover != True:
        print()


def satunnaiset(t, m):
    CRED = "\033[91m"
    CEND = "\033[0m"
    CGREEN = "\33[32m"
    roll = int(random.randint(1, 100))
    tired = t
    money = m
    if roll <= 20:
        tired += 20
        print(CRED + "Huono sää häiritsi untasi, väsymyksesi nousee 20" + CEND)
    elif roll > 20 and roll <= 40:
        tired += 30
        print(
            CRED
            + "'Onko täällä lääkäriä paikalla!?' Hätätapaus lentokoneessa stressaa sinua ja väsymyksesi nousee 30. "
            + CEND
        )
    elif roll > 50 and roll <= 60:
        tired += 50
        print(
            CRED
            + "Ruokamyrkytys! Voit pahoin etkä saa levättyä ollenkaan matkalla. Väsymyksesi nousee 50"
            + CEND
        )
    elif roll > 61 and roll <= 65:
        tired = 0
        print(
            CGREEN
            + "Löysit lennolta Finnairin mustikkamehua, joka virkistää sinua! Väsymyksesi nollautuu"
            + CEND
        )
    elif roll > 66:
        money += 200
        print(
            CGREEN
            + "Löysit femman maasta, joka tässä ekonomiassa on oikeasti 200 euroa!"
            + CEND
        )
    return tired, money


def väsymyksen_kokeilu(tired, time_spent):
    time = time_spent
    if tired > 100:
        print(
            "Olet liian väsynyt jatkaaksesi, sinun on pakko levätä ja menetät aikaa..."
        )
        input("Paina enter levätäksesi...")
        tired -= 75
        time += 12
        input("Olet levännyt 12 tuntia, voit jatkaa.")
        print(f"Väsymyksesi on nyt {tired}/100")
    return tired, time


# funktio joka antaa mahdollisen määränpään järjestysnumeron, mikäli sellainen on saavutettavissa
def has_common_item_with_values(list1, dict1):
    listaus = []
    numero = 0
    for i in dict1:
        listaus.append(dict1[i][2])
    for i in listaus:
        if i in list1:
            return listaus[numero]
        numero += 1
    return False


# köyhä
def köyhä():
    print(
        f"Köyhä, valitse halvempi vaihtoehto \n"
        f"Nykyinen rahatilanteesi on {money} euroa"
    )
    return


# lista välietapeista
destinations = ["LTFJ", "HECA", "VABB", "VECC", "VHHH", "RJTT", "KSFO", "KJFK", "EGGW"]

# asetetaan perusarvoja
total_travel_dist = 0
total_co2_spent = 0
money = 1000
tired = 0
time_spent = 0
current_ap = "KJFK"
game_id = create_game(money, current_ap, tired)
notover = True
# pelilooppi

read_highscores()
while True:
    # Otetaan nykyisen lentokentän info talteen
    airport = get_airport_info(current_ap)
    # tulostetaan pelaajalle näkyviin lentokenttä, raha ja väsy
    if airport:
        print(f"Olet {airport.get('name')}illa")
    print(f"Sinulla on rahaa {money} euroa")

    # pause
    input("Paina enter nähdäksesi mahdolliset matkustusvaihtoehdot")
    # pelaajalle esitellään matkustusvaihtoehdot
    valinta = ""
    while valinta != "tehty":
        print(
            f"Vaihtoehto 1. Ylimääräinen paikka itkevän vauvan vieressä Hinta: ilmainen Hidas Päästöt: korkeat Väsymys: Suuri "
        )
        print(
            f"Vaihtoehto 2. Ekonomialuokan paikka Hinta: 100e Nopea Päästöt: Normaalit Väsymys: Normaali"
        )
        print(
            f"Vaihtoehto 3. Premiumluokan paikka Hinta: 200e Nopeampi Päästöt: Pienemmät Väsymys: Normaali"
        )
        print(
            f"Vaihtoehto 4. Yksityissähkökone Hinta 300e Nopein Päästöt: Olemattomat Väsymys: Pieni"
        )
        # pelaajalta kysytään matkustusvaihtoehtoa
        question2 = input("Miten haluat matkustaa? (1. 2. 3. 4.)")
        if (
            question2 == "1"
            or not question2 == "2"
            or not question2 == "3"
            or not question2 == "4"
        ):
            if question2 == "1":
                tired += 25
                valinta = "tehty"
            if question2 == "2" and money >= 100:
                tired += 18
                money -= 100
                valinta = "tehty"
            if question2 == "2" and money < 100:
                köyhä()

            if question2 == "3" and money >= 200:
                tired += 18
                money -= 200
                valinta = "tehty"
            if question2 == "3" and money < 200:
                köyhä()

            if question2 == "4" and money >= 300:
                tired += 10
                money -= 300
                valinta = "tehty"
            if question2 == "4" and money < 300:
                köyhä()
            # pause
            if valinta == "tehty":
                input("Paina enter valitaksesi päämäärän")
    # peli hakee aiemmin määritellyllä funktiolla itäisemmät 9 lentokenttää, sekä kaikki itäisemmät kentät
    airports = get_easterner_ap(current_ap)
    checkforg = checkforgoal(current_ap)

    serial = 1
    # tarkistaa kaikki kentät idämpänä
    tarkistus = has_common_item_with_values(destinations, checkforg)
    # tarkistaa 9 lähintä kenttää
    tarkistus2 = has_common_item_with_values(destinations, airports)
    # peli tarkistaa aiemmin määriteltyjen funktioiden avulla onko 1000km päässä jokin välietappi
    if (
        tarkistus != False
        and calculate_distance(current_ap, tarkistus) < 1000
        or tarkistus2 != False
    ):
        print("Kohteesi on saavuettavissa")
        input(
            f"Paina enter matkustaaksesi {get_airport_info(tarkistus)['name']}ille, matkaa {calculate_distance(current_ap, tarkistus):.0f} kilometriä"
        )
        dest = tarkistus
    # peli tarkistaa onko nykyinen kenttä Tokiossa, josta ainut siirtymä on san franciscoon
    elif current_ap == "RJTT":
        print(
            "Olet saapunut Tokioon, Ainoa mahdollinen seuraava lentosi on San Franciscon kentälle"
        )
        input(
            f"Paina enter matkustaaksesi {get_airport_info('KSFO')['name']}ille, jolle matkaa {calculate_distance(current_ap, 'KSFO'):.0f} kilometriä"
        )
        dest = "KSFO"
    # peli tarkistaa onko nykyinen kenttä New Yorkin kenttä, ja asettaa notover ehdon falseksi, joka mahdollistaa pelin läpäisemisen
    elif current_ap == "KJFK":
        print(
            "Olet saapunut New Yorkiin ja nyt edessäsi on viimeinen lento takaisin Lontooseen, onnittelut"
        )
        input(
            f"Paina enter matkustaaksesi {get_airport_info('EGGW')['name']}ille, jolle matkaa {calculate_distance(current_ap, 'EGGW'):.0f} kilometriä"
        )
        dest = "EGGW"
        notover = False
    # peli tulostaa saavutettavissa olevat lentokentät, ja kysyy pelaajalta järjestysnumerolla mihin pelaaja haluaa matkata
    else:
        print(f"""Saavutettavissas olevat lentokentät: """)
        for i in airports:
            print(
                f"{serial}. {airports[i][1]} johon on matkaa {airports[i][0]:.0f} kilometriä {airports[i][2]}"
            )
            serial += 1
        while True:
            try:
                askdest = int(input("Anna kohteen järjestysnumero: "))
                if askdest > 9:
                    print("Liian iso numero, se on nyt 9")
                    askdest = 9
            except ValueError:
                print("Huono arvo, anna järjestysnumero: ")
            else:
                break
        dest = airports[int(askdest)][2]
        print(dest)

    # peli laskee valitulla matkustusvaihtoehdolla tehtyyn matkaan kuluneen ajan ja päästöt
    total_travel_dist += calculate_distance(current_ap, dest)
    if question2 == "1":
        time_spent += ((calculate_distance(current_ap, dest) / 850) + 3) * 1.2
        total_co2_spent += (calculate_distance(current_ap, dest) * 155 / 1000) * 2
    elif question2 == "2":
        time_spent += ((calculate_distance(current_ap, dest) / 850) + 3) * 1.0
        total_co2_spent += (calculate_distance(current_ap, dest) * 155 / 1000) * 2
    elif question2 == "3":
        time_spent += ((calculate_distance(current_ap, dest) / 850) + 3) * 0.8
        total_co2_spent += (calculate_distance(current_ap, dest) * 155 / 1000) * 2
    elif question2 == "4":
        time_spent += ((calculate_distance(current_ap, dest) / 850) + 3) * 0.6
        total_co2_spent += (calculate_distance(current_ap, dest) * 155 / 1000) * 0
    # peli päivittää tietokantaan sijainnin
    update_location(dest, tired, money, game_id)
    # peli asettaa määränpään nykyiseksi sijainniksi
    current_ap = dest
    # pelin "voitto" tarkistaa että new yorkissa on käyty (notover=False) ja että olemme saapuneet takaisin lontoon kentälle
    if notover == False and current_ap == "EGGW":
        total_travel_dist += calculate_distance(current_ap, dest)
        update_location(dest, tired, money, game_id)
        current_ap = dest
        # loppu fanfaarit pelaajalle, tulos tallentuu highscorena tietokantaan
        print(
            f"Tervetuloa takaisin, olet nyt suorittanut haaveesi, mutta nyt tulit miettineeksi toimintasi ympäristövaikutuksia."
        )
        print(f"Totaalimatkaa kuljit: {total_travel_dist:.0f} kilometriä")
        print(
            f"Lopputulokseksi kulutit: {total_co2_spent:.0f} kiloa hiilidioksidia ja aikaa kului {time_spent/24:.0f} päivää "
        )
        input("Paina enter tallentaaksesi suorituksesi tiedot tietokantaan")
        break
    sattuma = satunnaiset(tired, money)
    money = int(sattuma[1])
    tired = int(sattuma[0])

    print(f"Totaalimatkaa kuljettu: {total_travel_dist:.0f} kilometriä")
    print(f"Aikaa käytetty: {time_spent:.0f} tuntia")
    print(f"Väsymyksesi on {tired} / 100")
    sleepy = väsymyksen_kokeilu(tired, time_spent)
    tired = sleepy[0]
    time_spent = sleepy[1]
    lepo = input("Haluatko levätä? lepäämiseen kuluu aikaa 8h (Y/N)")
    if lepo.lower() == "y":
        print("Uinut 8 tuntia, väsymyksesi laskee 75")
        tired -= 75
        if tired < 0:
            tired = 0
        time_spent += 8
        print(f"Väsymyksesi on {tired} / 100")
        input("Paina enter jatkaaksesi")

record_highscore(total_travel_dist, total_co2_spent, time_spent, game_id)
read_highscores()


# easterner_ap = get_easterner_ap()
# numero = 0
# for i in easterner_ap:
#    print(f"{easterner_ap[i][1]} johon on matkaa {easterner_ap[i][0]} kilometriä")
#
