# Wir importieren die Module, die wir brauchen.

import sounddevice
import soundfile
import time

# Wir legen die Aufnahmelänge und die Qualität fest.

duration = 3
samplerate = 44100

# Wir nehmen auf. 

aufnahme_1 = sounddevice.rec(duration*samplerate, samplerate=samplerate, channels=2)
print("Aufnahme läuft.")
time.sleep(duration)

# Wir speichern eine .wav Datei.

soundfile.write("Aufnahme_1.wav",aufnahme_1, samplerate)
print("Okay, ich bin fertig! :) ")