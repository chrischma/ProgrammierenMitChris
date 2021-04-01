import secrets

ZEICHEN = "QWERTZUIOASDFGHJKLYXCVBNMqwertzuioasdfghjkyxcvbnm123456789"

pw = str()
laenge = int(input("Bitte gib die Passwortlänge ein: "))

for _ in range(laenge):
    pw = pw+secrets.choice(ZEICHEN)

print(pw)
