# Dieser Quelltext entspricht im Wesentlichen einer Beispielanfrage aus der YouTube
# API Dokumentation in Kombination mit Ergänzungen von Corey Schaefer, der in einem Tutorial 
# einen Vorschlag gemacht hat, wie man den Prozess vereinfachen kann. 


# Die benötigsten Google-Module können über die folgenden Befehle
# installiert werden:
# pip3 install --upgrade google-api-python-client
# pip3 install google-auth-oauthlib 

import os
import pickle        
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Die client_secrets_file kann als JSON in der Api Console 
# heruntergeladen werden: 
# https://console.cloud.google.com/apis/dashboard?hl=de
client_secrets_file = 'client_secret_826946559557-r23eqjep2sguqdd5v4f92jmqadf8kea6.apps.googleusercontent.com.json'

# Hier wird festgelegt, welche Google API genutzt werden soll. 
# Hier ist das jetzt die YouTube API, die wiederum viele Unter-APIs 
# besitzt.
scopes = ['https://www.googleapis.com/auth/youtube']


# Jetzt wird geprüft, ob bereits Anmeldedaten (credentials) existieren.
# Falls die Authorisierungsdaten nicht existieren oder nicht
# mehr gültig sind, wird ein neues token angefordert oder das
# alte Token erneuert. 

credentials = None

# Existiert ein Token bereits als Datei, wird es einfach aus der Datei geladen. 
if os.path.exists('token.pickle'):
	print('loading credentials from file')
	with open ('token.pickle', 'rb') as token:
		credentials = pickle.load(token)

if not credentials or not credentials.valid:
	if credentials and credentials.expired and credentials.refresh_token:
		print('refreshing access token')
		credentials.refresh(Request())

	else:
		print('creating new access token')
		flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        	client_secrets_file, scopes)
		credentials = flow.run_console()


	# Abschließend werden die Credentials in einer Datei gespeichert.
	# Die Daten können beim späteren Nutzen des Skripts wiederverwendet
	# werden, bis sie ablaufen.

	with open('token.pickle', 'wb') as f:
		print('saving credentials')
		pickle.dump(credentials, f)


def main():

	# Hinweis aus der YouTube Api:
	# Für die Nutzung des Skripts im Rahmen von lokalen Tests, 
	# dann wird die HTTPS-Prüfung vorrübergehend abgeschaltet. 
	# Wichtig: Sollte vor der Veröffentlichung wieder aktiviert werden!
	os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

	# Hier wird festgelegt, welche API genau genutzt werden soll. 
	# Hier ist das die YouTube Api in der Version 3.
    api_service_name = 'youtube'
    api_version = 'v3'

    # Der YouTube API-Client wird eingerichtet und in der Variable
    # 'youtube' hinterlegt, um einfacher aufgerufen zu werden.
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # Hier wird die eigentliche Anfrage unter der Nutzung der
    # credentials an die API von YouTube gestellt.
    request = youtube.videos().list(

    	# part ist dabei eine Pflichtvariable. myRating ist ein
    	# weiterer (optionaler) Parameter. In dieser Anfrage wird
    	# abgerufen, was vom Nutzer geliked wurde.
        part='snippet,contentDetails,statistics',
        myRating='like'
    )

    # Der request muss ausgeführt werden und gibt eine response zurück. 
    response = request.execute()

    print(response)

if __name__ == '__main__':
    main()
