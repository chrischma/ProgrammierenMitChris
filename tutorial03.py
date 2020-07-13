import random

print("Hallo du süßer Rügenwalder-Prinz.")

adjektive = ["geschmeidig","groß", "wohlriechend","pfiffig", "attraktiv"]
koerperteile = ["Ohren","Füße", "Haare", "Augen", "Hände"]

zufallszahl = random.randint(0,4)
koerperteil_zufaellig = koerperteile[zufallszahl]

zufallszahl = random.randint(0,4)
adjektiv_zufaellig = adjektive[zufallszahl]

# Hier wird der String ausgegeben. Alternativ lässt sich das über f-Strings lösen.

print("Deine ",koerperteil_zufaellig, "sind sehr", adjektiv_zufaellig)

