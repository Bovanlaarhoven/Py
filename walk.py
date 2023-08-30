import keyboard
import pyautogui
import time

def main():
    key_to_press = 'a'
    running = True

    while running:
        if keyboard.is_pressed('num 7'):
            key_to_press = 'd'
            pyautogui.keyDown(key_to_press)
            pyautogui.mouseDown()
        elif keyboard.is_pressed('num 8'):
            key_to_press = 'a'
            pyautogui.keyDown(key_to_press)
            pyautogui.mouseUp()
        else:
            pyautogui.keyUp(key_to_press)
            pyautogui.mouseUp()

        if keyboard.is_pressed('num 9'):
            pyautogui.keyUp(key_to_press)
            pyautogui.mouseUp() 
            running = False

        time.sleep(0.1)

if __name__ == "__main__":
    main()
