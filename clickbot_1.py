import pyautogui


# can be used to get the current cursor position
def print_position():
    while True:
        print(pyautogui.position())


# is used to click a certain position 50 times
# (in this example: a useless button on theuselessbutton.com)
def click_button():
    for i in range(50):
        pyautogui.click(260, 408)
        print('click', i)


click_button()
