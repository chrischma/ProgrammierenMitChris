# pip install opencv-python
# pip install pyautogui
# Berechtigungen erteilen

import pyautogui

img = 'button.png'
button = pyautogui.locateCenterOnScreen(img, confidence=0.99)


def click_button(button):
    if not button:
        return 

    for i in range(10):
        pyautogui.click(button.x/2, button.y/2)
        print('click', i)


click_button(button)


