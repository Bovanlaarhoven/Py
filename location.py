import pyautogui
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        rgb = pyautogui.pixel(x, y)
        print(f"Clicked at ({x}, {y}) RGB: {rgb}")

listener = mouse.Listener(on_click=on_click)
listener.start()

listener.join()
