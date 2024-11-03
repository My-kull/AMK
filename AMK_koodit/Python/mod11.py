# Tehtävä 11.1


class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")


# Pääohjelma
aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_nro_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti_nro_6.tulosta_tiedot()


# Tehtävä 11.2


class Car:
    def __init__(self, license_plt, max_speed):
        self.license_plt = license_plt
        self.max_speed = max_speed
        self.cur_speed = 0
        self.trip_meter = 0

    def accelerate(self, speed_change):
        self.cur_speed += speed_change
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0

    def drive(self, hours):
        self.trip_meter += self.cur_speed * hours


class Sahkoauto(Car):
    def __init__(self, license_plt, max_speed, akkukapasiteetti):
        super().__init__(license_plt, max_speed)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Car):
    def __init__(self, license_plt, max_speed, bensatankin_koko):
        super().__init__(license_plt, max_speed)
        self.bensatankin_koko = bensatankin_koko


# Pääohjelma
sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

# Asetetaan nopeudet
sahkoauto.accelerate(100)
polttomoottoriauto.accelerate(120)

# Ajetaan kolme tuntia
sahkoauto.drive(3)
polttomoottoriauto.drive(3)

# Tulostetaan matkamittarilukemat
print(f"Sähköauton matkamittarilukema: {sahkoauto.trip_meter} km")
print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.trip_meter} km")
