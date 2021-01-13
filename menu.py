from simple_term_menu import TerminalMenu

def menu():
	m = TerminalMenu(["Auswahl 1","Auswahl 2"],"Hauptmenü")
	auswahl = m.show()

	if auswahl == 0:
		print("Glückwunsch, du hast Auswahl 1 gewählt.")

	if auswahl == 1:
		print("Sehr schön, Auswahl 2!")

menu()
