import random

# Tehtävä 9.1 - Luokka


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


def new_car(license_plt, max_speed):
    return Car(license_plt, max_speed)


main_car = new_car("ABC-123", 142)
print(f"Licenseplate: {main_car.license_plt}, Max speed: {main_car.max_speed}")

# Tehtävä 9.2 - Auton kiihdytys ja matka

main_car.accelerate(30)
main_car.accelerate(70)
main_car.accelerate(50)
print(f"Current speed: {main_car.cur_speed}")
main_car.accelerate(-200)
print(f"Current speed after emergency braking: {main_car.cur_speed}")

# Tehävä 9.3 - Auton matka

main_car.accelerate(60)
main_car.drive(1.5)
print(f"Trip meter after 1.5 hours at 60 km/h: {main_car.trip_meter}")

# Tehtävä 9.4 - Autokilpailu

cars = []
for i in range(1, 11):
    license_plt = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(new_car(license_plt, max_speed))

race_finished = False
while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.trip_meter >= 10000:
            race_finished = True

# Tulosta tulokset
print(
    f"{'License Plate':<14} {'Max Speed':<10} {'Current Speed':<14} {'Trip Meter':<10}"
)
for car in cars:
    print(
        f"{car.license_plt:<14} {car.max_speed:<10} {car.cur_speed:<14} {car.trip_meter:<10}"
    )

# Moduuli 10

# Laitoin kielen erottamaan tehtävät toisistaan


class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")


# Talo-luokka
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.hissit[0].alin_kerros)


# Kilpailu-luokka
class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            speed_change = random.randint(-10, 15)
            auto.accelerate(speed_change)
            auto.drive(1)

    def tulosta_tilanne(self):
        print(
            f"{'License Plate':<14} {'Max Speed':<10} {'Current Speed':<14} {'Trip Meter':<10}"
        )
        for auto in self.autot:
            print(
                f"{auto.license_plt:<14} {auto.max_speed:<10} {auto.cur_speed:<14} {auto.trip_meter:<10}"
            )

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.trip_meter >= self.pituus:
                return True
        return False


# Pääohjelma
if __name__ == "__main__":
    # Testataan Hissi- ja Talo-luokat
    talo = Talo(1, 10, 3)
    talo.aja_hissiä(0, 5)
    talo.aja_hissiä(1, 7)
    talo.palohälytys()

    # Kilpailu
    cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
    kilpailu = Kilpailu("Suuri romuralli", 8000, cars)

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1
        if tunti % 10 == 0:
            kilpailu.tulosta_tilanne()

    kilpailu.tulosta_tilanne()
    print("Kilpailu on päättynyt!")
