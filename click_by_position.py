from pyautogui import click, position

x = 260
y = 408


def print_position():
    while True:
        print(position())


def click_button(x, y):
    for i in range(50):
        click(x, y)
        print(f'click {i}')


click_button(x, y)
