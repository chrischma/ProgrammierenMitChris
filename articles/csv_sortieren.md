# Tutorial: CSV-Dateien umsortieren und speichern

Pfaelzer hat gefragt, wie man csv-Dateien mit Python sortieren und speichern kann. Und genau das machen wir heute. Ich bin Chris und das ist programmieren mit Chris. Viel Spaß.

Um das Problem zu lösen, müssen wir drei Dinge tun. 

*  Wir müssen eine die-Datei einlesen
*  Wir müssen die Daten umsortieren
*  ... und anschließend aus den sortierten Daten eine csv-Datei erstellen.

Und für all das nutzen wir Pandas. Nein, nicht diese Pandas, sondern dieses Pandas. Pandas ist ein Python-Modul, das bei der Analyse von größeren Datensätzen ungemein hilfreich ist. 

[Projekt einrichten; ]

Wie immer beginnen wir damit, dass wir uns Pandas installieren. Dafür gehe ich in meine Konsole und tippe ein:

`pip3 install pandas`

Das Modul ist installiert und jetzt kann ich es in mein Projekt importieren. Dafür schreibe ich 

`import pandas`

Als nächstes lese ich meine csv-Datei mit Pandas ein und speichere sie in einer Variable.

`data = pandas.read_csv('worldcities.csv')`

Jetzt sortieren wir die Daten. Auch dafür lege ich eine neue Variable an. 

`sorted_data = data.sort_values(by=['city'], ascending=True)`

Ascending bedeutet übrigens 'aufsteigend'. 

Und jetzt da unsere Daten sortiert sind, können wir sie in eine neue csv-Datei schreiben.

`sorted_data.to_csv('worldcities_by_city.csv')`

Das funktioniert schon mal - und theoretisch können wir jetzt Feierabend machen, wenn wir so mit den Daten zufrieden sind.

Zwei Sachen sind jedoch noch ein bisschen problematisch, wenn wir die beiden csv-Dateien miteinander vergleichen. Und ich zeig euch noch kurz, wie ihr diese Problemchen lösen könnt. Einerseits fehlen die Anführungszeichen, die wir noch in der ursprünglichen Datei hatten. Und die können wir uns über den Befehl `quoting=1` wiederherstellen. 

`sorted_data.to_csv('worldcities_by_city.csv', quoting=1)`

[**Kontrollieren**]

Und noch eine Sache ist auffällig. Pandas hat hier noch eine seltsame erste Spalte hinzugefügt. Das ist eine sogenannte Index-Spalte. Pandas nummeriert nämlich beim Einlesen alle Zeilen der Tabelle. Und diese Nummerierung schreibt Pandas auch in die neue csv-Datei. Wenn wir nicht wollen, dass diese Nummerierung in der neuen Datei auftaucht, können wir auch das mit einem zusätzlichen Parameter bewerkstelligen. Und das ist der `index`-Parameter: 

`sorted_data.to_csv('worldcities_by_city.csv', quoting=1, index=False)`

Und jetzt sehen die Daten super aus und wir haben es geschafft. 

Okay, soviel erstmal für heute. Fragen und Wünsche könnt ihr wie immer in der Kommentarspalte dalassen, ich antworte bei passenden Fragen mit kurzen Videoantworten. Und jetzt viel Spaß beim Ausprobieren, bleibt neugierig und bis bald! 

## ✅ Kompletter Quellcode

```python
import pandas

data = pandas.read_csv('worldcities.csv')
sorted_data = data.sort_values(by=['city'], ascending=True)
sorted_data.to_csv('worldcities_by_city.csv', quoting=1, index=False)

```

