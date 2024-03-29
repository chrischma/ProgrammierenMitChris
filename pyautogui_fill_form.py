'''
purpose of this script is to fill out this form:
https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit
'''

from pyautogui import write, press, hotkey, click
from time import sleep


def fill_form(first_name, last_name):
    click(516, 373, clicks=3)
    sleep(1)
    
    press('backspace', 10)
    write(first_name)

    press('tab')
    write(last_name)

    press('tab')
    press('space')

    hotkey('command','r')
    sleep(1)


# Example data
names = ['Bernd Stromberg', 'Ulf Steinke', 'Berthold Heisterkamp']

for name in names:
    first_name, last_name = name.split(' ')
    fill_form(first_name, last_name)
