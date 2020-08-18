from tkinter import *

main = Tk()

slider = Scale(main, from_=0, to=100, orient=HORIZONTAL)

def get_value():
	value = slider.get()
	print(value)

button = Button(main, text="Hey, gib den Wert", command=get_value)

slider.pack()
button.pack()

mainloop()