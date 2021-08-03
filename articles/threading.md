# Python Threading - Mehrere Funktionen parallel ausführen



Wenn ihr wissen wollt. wie man mit Python mehrere Funktionen parallel ausführen kann, dann seid ihr hier genau richtig. Ich bin Chris und das ist Programmieren mit Chris - viel Spaß. 

Normalerweise läuft ein Python Programm Schritt für Schritt ab. Python schnappt sich also die erste Aufgabe, arbeitet sie ab und geht dann zur nächsten Aufgabe weiter. Man sagt auch, dass Python in einem sogenannten Thread, also in einem Kanal oder Gang läuft. 

Das Schöne ist, dass wir mehrere dieser Threads erstellen können, wenn wir wissen wie. Und genau dafür nutzen wir das Modul THREADING.

Schauen wir uns an, wie das in der Praxis funktioniert.

Als erstes Schreiben wir ein kleines Programm, das aus zwei einfachen Funktionen besteht. Die beiden Funktionen sollen nichts anderes machen als immer wieder sagen, dass sie gerade laufen. 

```python
import time


def funktion_1():
    while True:
        print("Funktion 1 läuft")
        time.sleep(1)

        
def funktion_2():
    while True:
        print("Funktion 2 läuft")
        time.sleep(2)
        
        
funktion_1()
funktion_2()
```

Wenn wir das Skript jetzt abfeuern, stellen wir fest, dass nur die erste Funktion aufgerufen wird. Und das liegt daran, dass Python die Funktion erst zuende aufrufen möchte, bevor Python weiter zur zweiten Funktion geht. Da können wir jetzt aber bis uns graue Haare wachsen, weil die erste Funktion ja unendlich lange ausgeführt wird. 

Machen wir uns deshalb jetzt daran, die beiden Funktionen gleichzeitig auszuführen. Dafür nutzen wir das Threading Modul. Das ist vorinstalliert, wir können es also direkt importieren und nutzen. 

`from threading import Thread`

Jetzt definieren wir einen neuen Thread und legen fest, welche Funktion in diesem Thread laufen soll. Das gleiche machen wir auch gleich für die zweite Funktion.

```python
thread_1 = Thread(target=funktion_1)
thread_2 = Thread(target=funktion_2)
```

Jetzt haben wir es fast geschafft. Wir müssen die Threads nur noch starten. 

```python
thread_1.start()
thread_2.start()
```

Okay, soviel erstmal für heute. Fragen und Wünsche könnt ihr wie immer in der Kommentarspalte dalassen, ich antworte bei passenden Fragen mit kurzen Videoantworten. Wenn ihr den Kanal unterstützen wollt, dann findet ihr alle Infos dazu in der Videobeschreibung. Und jetzt viel Spaß beim Ausprobieren, bleibt neugierig und bis bald! 

## ✅ Kompletter Quellcode

```python
import time
from threading import Thread


def funktion_1():
    while True:
        print("Funktion 1 läuft")
        time.sleep(1)


def funktion_2():
    while True:
        print("Funktion 2 läuft")
        time.sleep(1)


thread_1 = Thread(target=funktion_1)
thread_2 = Thread(target=funktion_2)

thread_1.start()
thread_2.start()

```

