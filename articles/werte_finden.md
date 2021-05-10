# Kleinste und größte Werte einer Liste finden mit Python

Mein Zuschauer *PyQGis* hat gefragt, wie herausfinden kann, an welcher Position sich das kleinste Element einer Liste befindet. Um das Problemchen zu lösen, müssen wir eigentlich nur zwei Dinge tun. Wir müssen zuerst das kleinste Element finden und in einem zweiten Schritt dessen Position ermitteln. 
Ihr seht, ich hab hier schon eine Liste angelegt. Die heißt einfach `coole_liste`:

`coole_liste = [29, 87, 467, 2, 57]` 

In Python können wir uns das kleinste Element über die Funktion `min()` anzeigen lassen. Dafür schreibe ich:

`min(coole_liste)`

Diesen Wert will ich später noch verwenden, deshalb gebe ich ihm einen Namen. 

`kleinster_wert = min(coole_liste)`

Und jetzt schauen nach, wo sich das Element befindet. Daür nutzen wir die `index`- Funktion. Und die funktioniert so: Ich gebe zuerst die Liste an, um die es geht, dann das Wort `index` und dann den Wert, dessen Position ich finden möchte.

`coole_liste.index(kleinster_wert)`

Und auch diesen Wert will ich in einer Variable speichern.

`pos_min = coole_liste.index(kleinster_wert)`

Und jetzt kann ich mir das Ganze auch schon ausgeben lassen. Das funktioniert übrigens genauso einfach mit der größten Zahl. Dafür muss ich einfach statt der `min()`-Funktion die `max()-Funktion nutzen. Unser fertiger Quellcode sieht jetzt so aus:

```python
coole_liste = [29, 87, 467, 2, 57]

kleinster_wert = min(coole_liste)
groesster_wert = max(coole_liste)

pos_min = coole_liste.index(kleinster_wert)
pos_max = coole_liste.index(groesster_wert)

print(pos_min, pos_max)

```

