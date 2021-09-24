import tkinter as tk

window = tk.Tk()
window.geometry('200x100')

input_string = tk.StringVar()
user_input_field = tk.Entry(window, textvariable=input_string)
output_label = tk.Label(window, textvariable=input_string)
ok_button = tk.Button(text='Ok', command=lambda: show_user_input())

user_input_field.pack()
output_label.pack()
ok_button.pack()


def show_user_input():
    user_input = user_input_field.get()
    print('Du hast eingegeben: ' + user_input)


window.mainloop()
