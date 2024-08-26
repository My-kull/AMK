#teht 3.1
# Kysyy käyttäjältä kuhan pituuden
kuhanpituus = float(input("Anna kuhan pituus senttimetreinä: "))
minpit = 37
# Tarkistaa onko kuha tarpeeksi iso
if kuhanpituus < minpit:
    print(f"Kuha on alimitoitettu. Tarvitset vielä {minpit - kuhanpituus:.2f} cm.")
else:
    print("Kuha on sallittu.")

#teht 3.2
# Kysyy käyttäjältä hyttiluokan
hytti = input("Minkä tyyppinen hytti? (LUX, A, B, C): ")
# Hyttien tiedot
LUX = "LUX on parvekkeellinen hytti yläkannella."
A = "A on ikkunallinen hytti autokannen yläpuolella."
B = "B on ikkunaton hytti autokannen yläpuolella."
C = "C on ikkunaton hytti autokannen alapuolella."
# Tarkistaa hyttiluokan ja tulostaa tiedot
if hytti == "LUX":
    print(LUX)
elif hytti == "A":
    print(A)
elif hytti == "B":
    print(B)
elif hytti == "C":
    print(C)
else:
    print("Virheellinen hyttiluokka.")

#teht 3.3
# Kysyy sukupuolen, sekä hemoglobiiniarvon
sukupuoli = input("Mikä on sukupuolesi? (M/N): ")
hemoglobiini = float(input("Mikä on hemoglobiiniarvosi? (g/l) "))
# Tarkistaa sukupuolen ja hemoglobiiniarvon
if (sukupuoli == "M") and (hemoglobiini >=134 and hemoglobiini <=195):
    print(f"Hemoglobiiniarvo {hemoglobiini:.2f}g/l sukupuolelle {sukupuoli} on normaali.")
elif (sukupuoli == "M") and (hemoglobiini <134):
    print(f"Hemoglobiiniarvo {hemoglobiini:.2f}g/l sukupuolelle {sukupuoli} on alhainen.")
elif (sukupuoli == "M") and (hemoglobiini >195):
    print(f"Hemoglobiiniarvo {hemoglobiini:.2f}g/l sukupuolelle {sukupuoli} on korkea.")
elif (sukupuoli == "N") and (hemoglobiini >=117 and hemoglobiini <=175):
    print(f"Hemoglobiiniarvo {hemoglobiini:.2f}g/l sukupuolelle {sukupuoli} on normaali.")
elif (sukupuoli == "N") and (hemoglobiini <117):
    print(f"Hemoglobiiniarvo {hemoglobiini:.2f}g/l sukupuolelle {sukupuoli} on alhainen.")
elif (sukupuoli == "N") and (hemoglobiini >175):
    print(f"Hemoglobiiniarvo {hemoglobiini:.2f}g/l sukupuolelle {sukupuoli} on korkea.")
else:
    print("Virheellinen syöttö.")

#teht 3.4
# Kysyy käyttäjältä vuosiluvun
vuosi = int(input("Anna vuosiluku: "))
# Tarkistaa onko vuosi karkausvuosi
if vuosi % 400 == 0 and vuosi % 100 == 0:
    print(f"Vuosi {vuosi} on karkausvuosi.")
elif vuosi % 100 != 0 and vuosi % 4 == 0:
    print(f"Vuosi {vuosi} on karkausvuosi.")
else:
    print(f"Vuosi {vuosi} ei ole karkausvuosi.")
