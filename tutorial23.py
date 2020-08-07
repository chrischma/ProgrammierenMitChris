import os

def siri_say(text):
	formatierter_text = f'say {text}'
	print(formatierter_text)
	os.system(formatierter_text)

siri_say("Wow! Es hat funktioniert!")
