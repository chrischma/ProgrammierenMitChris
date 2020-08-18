# matplotlib.pyplot importieren
import matplotlib.pyplot as plt 		

# Daten anlegen
monate = ["Mai","Jun","Juli","August"]
abos = [0,3,4,7]

# Plot erzeugen
plt.plot(monate,abos)					

# Zusätzlich speichern wir das ganze als Grafik ab und geben der Grafik einen Namen.
plt.savefig("meine_Abos")   			 
