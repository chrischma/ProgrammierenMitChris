# Tutorial: NASA-Daten mit Python auslesen

Im heutigen Tutorial sollte sich eigentlich alles um den Mars drehen. Ich wollte euch heute nämlich eigentlich zeigen, wie man mit Hilfe eines Python Skriptes das aktuelle Wetter auf dem Mars auslesen kann. Aber wie das immer so ist: Der NASA sind ihre Sensoren um die Ohren geflogen und deshalb gibt es bis auf weiteres keine Daten mehr, und somit auch kein Wetterbericht vom Mars. 

Die gute Neuigkeit: Auch auf der Erde gibt es über Daten der Nasa mehr als genug spannende Sachen zu entdecken. Und genau das machen wir heute. Ich bin Chris, und das ist Programmieren mit Chris. Viel Spaß. 

Die Nasa stellt  viele ihrer Daten öffentlich über eine sogenannte API zur Verfügung. So eine API ist eine Schnittstelle zwischen uns und einem Datenanbieter, also z.B. der Nasa. 

Auf der Website der Nasa finden wir sogar gleich eine ganze Menge von verschiedenen APIs, mit denen man jeweils andere Daten abrufen kann. Für uns ist heute die **EONET API** interessant. Die sammelt alle größeren Naturereignisse auf der Erde, also Zyklone,  Waldbrände oder auch Vulkanausbrüche. Und als kleines Beispiel schreiben wir heute ein Skript, das uns alle Ereignisse innerhalb des letzten Jahres anzeigt.

Wir beginnen damit, dass wir uns die benötigten Module installieren. Dafür gehe ich in mein Terminal und tippe ein:

`pip3 install requests`

Das Modul ist installiert und wir können es jetzt importieren.

``` python
import requests
import json
```



Als nächstes stellen wir eine Anfrage an den Server der Nasa. Und damit wir die Anfrage auf die richtige Art und Weise stellen, müssen wir uns anschauen, was für eine Anfrage der Server der Nasa erwartet. Informationen zur Funktionsweise einer API stehen normalerweise in der sogenannten API-Dokumentation. 

`https://eonet.sci.gsfc.nasa.gov/docs/v2.1`

Und in den meisten Dokumentationen finden wir Beispielanfragen wie diese hier:

`https://eonet.sci.gsfc.nasa.gov/api/v2.1/events`

So eine API Anfrage siehst erstmal aus wie eine Internetadresse, enthält aber zusätzlich einige Parameter. Parameter sind Schlüsselwörter, die wir an die Anfrage einfach mit ranhängen können. Und mit denen sagen wir dem Server, was genau wir an Daten anfragen wollen. Zwei Parameter sind für uns besonders interessant: `limit` und `days`. Mit `limit` legen wir fest, wieviele Ergebnisse wir haben wollen. Und mit `days` können wir (wenig überraschend) festlegen, für wieviele Tage wir die Daten haben möchten. 

Beide Parameter können wir schon einmal in unserem Skript aufschreiben. 

```python
limit = 500
days = 356
```

Und wenn wir schon dabei sind, nehmen wir uns auch schon mal diese Beispielanfrage mit. 

`url = https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?limit=5&days=20&source=InciWeb&status=open`

Und damit Python weiß, dass es sich um eine Zeichenkette handelt, schreiben wir vor die Adresse ein f und setzen die gesamte Adresse in Anführungsstrichen. 

`url = f'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?limit=5&days=20&source=InciWeb&status=open'`

Jetzt ersetzen wir die Parameter, die schon in der Adresse stehen durch unsere eigenen Werte.

`url = f'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?limit={limit}&days={days}'`

Unsere Anfrage ist startklar und jetzt schicken wir sie an den Server der Nasa.

Anfrage:`r = requests.get(url)` 

Antwort des Servers: `<Response [200]>`

Damit wir das, was uns der Server zurückgeschickt hat, lesen können, wandeln wir die Serverantwort in das JSON-Format um.  JSON ist ein besonders einfaches, leicht lesbares Format, das wir gleich leicht durchsuchen können.

`events_data = r.json()`

Diese Daten speichern wir uns auch gleich in einer eigenen json-Datei, damit sie nicht verloren gehen. Dafür öffnen wir zunächst eine neue Datei und sagen, dass wir in der Datei schreiben wollen:

`with open('events.json','w') as f:`

Und während die Datei offen ist, schreiben wir in sie unsere Daten. 

`    f.write(json.dumps(events_data, indent=4))`

Mit dem Begriff `dumps` werden unsere Daten in eine JSON-Zeichenkette umgeformt. Und mit `indent=4` legen wir fest, wie groß die Einrückungen zwischen den einzelnen Elementen sein sollen. 

In der JSON Datei suchen wir jetzt nach dem Teil der Daten, der uns interessiert. Einzelne Objekte werden bei JSON durch geschwungene Klammern gekennzeichnet. Und die Objekteigenschaften können wir an den Anführungszeichen erkennen. Wir können hier jetzt sehen, dass unsere json Datei ein Objekt enthält (das sehen wir an der ersten Klammer) und dieses Objekt hat verschiedene Eigenschaften. Es hat z.B. einen Titel und eine Beschreibung.

Für uns ist jetzt vor allem die Eigenschaft `events ` interessant. `events ` enthält nämlich selbst wieder Objekte, was ihr an den geschwungenen Klammern erkennen könnt. Und diese Objekte sind genau das, was wir suchen, weil jedes Objekt in Events für ein Ereignis steht, das dokumentiert wurde, also z.B. einen Vulkanausbruch oder einen Waldbrand. In jedem Fall ist also schon mal der Teil `events`für uns der spannende, deshalb speichern wir uns Events schon mal in einer eigenen Variable. 

`event_list = events_data['events']`

Und jetzt folgt schon der letzte Schritt. Wir lassen uns jetzt alle Elemente der Liste ausgeben. 

```python
for event in event_list:
    print(event['title'])
```

Okay, soviel erstmal für heute. Viel Spaß beim Ausprobieren, bleibt neugierig und bis bald! 

## ✅ Kompletter Quellcode

```python
import requests
import json

limit = 500
days = 356

url = f'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?limit={limit}&days={days}'
r = requests.get(url)
events_data = r.json()
event_list = events_data['events']

# with open('events.json','w') as f:
#    f.write(json.dumps(events_data, indent=4))

for event in event_list:
		# print(event)
    if 'fire' in str(event['categories']):
        print(event['title'])
      
```

