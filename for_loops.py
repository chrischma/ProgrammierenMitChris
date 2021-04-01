namen = ["Chris", "Gerda", "Alfred", "Lotte"]
preise = [9.99, 19.99, 2500, 12.99]

for name in namen:
    print(f'Hallo {name}')

for preis in preise:
    preis *= 0.8
    print(f'Der neue Preis beträgt jetzt {preis}')
    
