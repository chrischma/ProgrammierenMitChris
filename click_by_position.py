import pyautogui

def print_position():
    '''infinite function that prints x and y of the current cursor position'''
    while True:
        print(pyautogui.position())



def click_button():
    '''
    is used to click a certain position 50 times
    (in this example: a useless button on theuselessbutton.com)
    '''
    for i in range(50):
        pyautogui.click(260, 408)


click_button()
