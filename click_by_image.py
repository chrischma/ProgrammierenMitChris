import pyautogui


def click_button(image, scaling):
    for i in range(10):
        position = pyautogui.locateCenterOnScreen(image, confidence=0.90)

        if position:
            x, y = position
            x *= scaling 
            y *= scaling

            pyautogui.click(x, y)


scaling = 0.5     
image = 'button.png' 
click_button(image, scaling)
