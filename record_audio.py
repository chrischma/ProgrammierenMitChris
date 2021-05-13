import sounddevice
import soundfile
import time

duration = 3
samplerate = 44100

aufnahme_1 = sounddevice.rec(duration*samplerate, samplerate=samplerate, channels=2)
print("Aufnahme läuft.")
time.sleep(duration)

soundfile.write("Aufnahme_1.wav",aufnahme_1, samplerate)
print("Okay, ich bin fertig! :) ")
