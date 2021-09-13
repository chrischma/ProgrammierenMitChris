import tkinter as tk

contact_names = ['Oma Frieda', 'Heinz', 'Lotte']
contact_numbers = ['8482938', '+49 174923857', '11833']


def display_number_for_contact():
    selection_index = contact_listbox.curselection()[0]
    phone_number_of_contact = contact_numbers[selection_index]
    numbers_label['text'] = phone_number_of_contact


window = tk.Tk()
window.title('Mein Telefonbuch')
window.geometry('300x300')
window.config(bg="lightblue")

numbers_label = tk.Label(text='Hallo!')
numbers_label.config(font=("Arial", 20, "bold"), bg="lightblue")

contact_names_var = tk.StringVar(value=contact_names)
contact_listbox = tk.Listbox(window, height=10, listvariable=contact_names_var)
contact_listbox.bind('<<ListboxSelect>>', lambda e: display_number_for_contact())

numbers_label.pack(pady=10)
contact_listbox.pack()

window.mainloop()
