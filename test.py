import pyautogui

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

while True:
    if pyautogui.position() == (0, 0):
        print("Mouse is at (0, 0).")
    else:
        pyautogui.moveTo()
