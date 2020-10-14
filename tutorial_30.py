import secrets

pw = ""
zeichen = "QWERTZUIOASDFGHJKLYXCVBNMqwertzuioasdfghjkyxcvbnm123456789" 
laenge = int(input("Bitte gib die Passwortlänge ein: "))

for _ in range(laenge):
	pw = pw+secrets.choice(zeichen)

print(pw)

