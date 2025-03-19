from flask import Flask, request
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="surviver",
    password="123",
    database="flight_game",
    charset="latin1",
    collation="latin1_swedish_ci",
)

# Tehtävä 13.1


app = Flask(__name__)


@app.route("/isPrime/<num>")
def primer(num):
    luku = int(num)
    isPrime = True

    if luku < 2:
        isPrime = False
    if luku in (2, 3):
        isPrime = True
    if luku % 2 == 0 or luku % 3 == 0:
        isPrime = False

    i = 5
    while i * i <= luku:
        if luku % i == 0 or luku % (i + 2) == 0:
            isPrime = False
        i += 6

    vastaus = {"Number": luku, "isPrime": isPrime}

    return vastaus


# Tehtävä 13.2


@app.route("/airport/<ICAO>")
def airport(ICAO):
    Name = "Name"
    Municipality = "Municipality"

    vastaus = {"ICAO": ICAO, "Name": Name, "Municipality": Municipality}

    return vastaus


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
