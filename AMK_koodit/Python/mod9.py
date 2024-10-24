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
