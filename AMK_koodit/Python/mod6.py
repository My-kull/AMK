import random
#teht 6.1
# Funktio palauttaa satunnaisen numeron väliltä 1-6
def roll_dice():
    return random.randint(1, 6)

def dice_loop():
    while True:
        # Kutsuu roll_dice funktiota ja tallentaa tuloksen muuttujaan
        roll = roll_dice()
        # Tulostaa muuttujan arvon
        print(roll)
        # Jos muuttujan arvo on 6, looppi päättyy
        if roll == 6:
            break

# Kutsuu funktiota
dice_loop()


#teht 6.2
# Funktio palauttaa satunnaisen numeron annetun parametrin mukaan
def roll_dice_mod(num_faces):
    return random.randint(1, num_faces)

def dice_loop_mod(num_faces):
    while True:
        roll = roll_dice_mod(num_faces)
        print(roll)
        if roll == num_faces:
            break

# Pyydä käyttäjältä suurin nopan tahkon arvo
max_face_value = int(input("Anna nopan suurin tahkon arvo: "))

# Kutsu funktiota käyttäjän syötteen kanssa
dice_loop_mod(max_face_value)


#teht 6.3
# Funktio, joka muuntaa gallonat litroiksi
def gallons_to_liters(gallons):
    return gallons * 3.785

def convert_gallons_to_liters():
    while True:
        # Kysy käyttäjältä gallonamäärä
        gallons = float(input("Anna bensiinin määrä Yhdysvaltain nestegallonoissa: "))
        # Jos käyttäjä syöttää negatiivisen määrän, lopeta muuntaminen
        if gallons < 0:
            break
        # Muunna gallonat litroiksi ja tulosta tulos
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallonaa on {liters} litraa.")

# Kutsu funktiota
convert_gallons_to_liters()


#teht 6.4
# Funktio laskee listan numeroiden summan
def sum_of_list(numbers):
    return sum(numbers)

def summer():
    # Luo tyhjän listan
    numbers = []
    while True:
        # Pyydä käyttäjältä numero
        number = int(input("Anna numero (0 lopettaa): "))
        # Jos käyttäjä syöttää nollan, katkaise silmukka
        if number == 0:
            break
        # Lisää numero listaan
        numbers.append(number)
    # Kutsu funktiota ja tallenna tulos
    sum_numbers = sum_of_list(numbers)
    # Tulosta summa
    print(f"Listan lukujen summa on {sum_numbers}.")

# Kutsu pääohjelmaa
summer()


#teht 6.5
# Funktio poistaa parittomat numerot listasta
def remove_odd_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

def test_remove_odd_numbers():
    # Luo tyhjän listan
    numbers = []
    while True:
        # Pyydä käyttäjältä numero
        number = int(input("Anna numero (0 lopettaa): "))
        # Jos käyttäjä syöttää nollan, katkaise silmukka
        if number == 0:
            break
        # Lisää numeron listaan
        numbers.append(number)
    # Kutsuu funktiota, joka poistaa parittomat numerot ja tallentaa tuloksen muuttujaan
    even_numbers = remove_odd_numbers(numbers)
    # Tulostaa sekä alkuperäinen että karsitun listan
    print(f"Alkuperäinen lista: {numbers}")
    print(f"Karsittu lista: {even_numbers}")

# Kutsu pääohjelmaa
test_remove_odd_numbers()


#teht 6.6
# Funktio, joka laskee pizzan hinnan neliömetriä kohden
def pizza_unit_price(diameter, price):
    radius = diameter / 2
    area = 3.14159 * radius * radius
    return price / area

def compare_pizzas():
    # Pyydä käyttäjältä kahden pizzan halkaisija ja hinta
    diameter1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
    price1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))
    diameter2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
    price2 = float(input("Anna toisen pizzan hinta euroina: "))

    # Laske pizzojen yksikköhinnat
    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    # Vertaa yksikköhintoja ja tulostaa tuloksen
    if unit_price1 < unit_price2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif unit_price1 > unit_price2:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat antavat saman vastineen rahalle.")

# Kutsuu funktiota
compare_pizzas()
