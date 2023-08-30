import pyautogui
import time

def hold_key(key, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        pyautogui.keyDown(key)
        time.sleep(0.01)
        pyautogui.keyUp(key)

if __name__ == "__main__":
    print("Press 'Ctrl+C' to exit the script.")
    while True:
        if pyautogui.keyDown('ctrl') and pyautogui.press('c'):
            print("Exiting the script.")
            break

        pyautogui.mouseDown()  # Hold left mouse button
        hold_key('d', 250)     # Hold 'd' key for 250 seconds
        hold_key('a', 250)     # Hold 'a' key for 250 seconds
        pyautogui.mouseUp()    # Release left mouse button
