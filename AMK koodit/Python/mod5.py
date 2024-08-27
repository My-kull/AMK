import random

#teht 5.1

# Alustetaan lista
temp = []

# Kysyy montako noppaa heitetään ja montako sivua nopassa on
nopat = int(input("Kuinka monta noppaa heitetään? "))
sivut = int(input("Kuinka monta sivua nopassa on? "))

# Looppi heittää noppia ja lisää tulokset listaan
for i in range(nopat):
    temp.append(random.randint(1, sivut))

# Tulostaa noppien summan
print(f"Noppien summa on {sum(temp)}")


#teht 5.2

# Alustetaan lista, johon kysytään ensimmäinen luku
temp = [float(input("Anna luku: "))]

# Looppi kysyy lukuja listaan, kunnes syöte on tyhjä
for i in temp:
    temp_num = input("Anna luku: ")
    if temp_num == "":
        break
    temp.append(float(temp_num))

# Järjestää listan isoimmasta pienimpään
temp.sort(reverse=True)

print("Max viisi isointa lukua ovat:")

# Looppi tulostaa viisi isointa lukua listasta
for i in range(len(temp)):
    if i >=5:
        break
    print (temp[i])


#teht 5.3

# Kysyy luvun
num = int(input("Anna luku: "))

# Alustetaan muuttuja, joka kertoo onko luku alkuluku
is_prime = True

# Looppi tarkistaa onko luku alkuluku
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

# Tulostaa onko luku alkuluku
if is_prime:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")


#teht 5.4
