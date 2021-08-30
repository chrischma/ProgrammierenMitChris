import tkinter


# --- SETTING UP THE WINDOW --- #
window = tkinter.Tk()
window.geometry('150x220')
window.title('Rechner')

gui_items = list()
button_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 '+', '-', '*', '/', '=', 'AC']


# --- CALCULATION AREA --- #
calculation = str()


def add_button_text_to_calculation(value):
    global calculation

    # AC (also known as 'ALL CLEAR') will clear the current calculation.
    if value == 'AC':
        calculation = str()
        output_label['text'] = '...'
        return

    if value == '=':
        calculate(calculation)
        calculation = str()
        return

    calculation = calculation + value
    output_label['text'] = calculation


def calculate(calc):
    try:
        result = eval(calc)
        print(result)
        output_label['text'] = result

    except Exception as e:
        print(e)
        output_label['text'] = 'Error'


# --- PREPARING THE GUI ITEMS --- #
def create_button(value):
    button = tkinter.Button(text=value, command=lambda: add_button_text_to_calculation(value))
    gui_items.append(button)


for val in button_values:
    create_button(val)


# --- PLACING THE GUI --- #
output_label = tkinter.Label(text='Hallo.')
output_label.grid(row=0, columnspan=10)

# All buttons will be auto-placed in a grid
# with maximum 3 columns and endless rows here:
column_count = 0
row_count = 1
maximum_columns = 3

for item in gui_items:
    item.grid(row=row_count, column=column_count)

    column_count += 1
    if column_count == maximum_columns:
        column_count = 0
        row_count += 1


if __name__ == '__main__':
    window.mainloop()
