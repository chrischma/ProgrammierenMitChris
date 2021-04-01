import telegram_send


def tel_send(msg):
    telegram_send.send(messages=[msg], conf="Uschi")


tel_send("Hallo hier ist die Uschi")
tel_send("Ist noch Kuchen da?")
tel_send("Schöne Grüße an Heinz!")
