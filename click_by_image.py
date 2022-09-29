from pyautogui import locateCenterOnScreen, click


def click_button(image, scaling):
    while True:
        position = locateCenterOnScreen(image, confidence=0.90)
        
        if position:
            break
        
    x, y = position
    x *= scaling 
    y *= scaling

    click(x, y)         


scaling = 0.5     
image = 'button.png' 
click_button(image, scaling)
