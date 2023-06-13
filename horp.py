import pyautogui
from pynput import keyboard

coordinates = [
    (848, 516),
    (882, 516),
    (919, 518),
    (958, 523),
    (992, 521),
    (1030, 523),
    (1064, 523)
]

previous_colors = {} 
is_pixel_checking = False

def check_and_click_pixels():
    for coord in coordinates:
        x, y = coord
        pixel_color = pyautogui.pixel(x, y)

        if coord not in previous_colors:
            previous_colors[coord] = pixel_color
            continue

        previous_color = previous_colors[coord]
        if pixel_color != previous_color:
            pyautogui.click(x, y)
            break

def on_press(key):
    global is_pixel_checking

    if key == keyboard.Key.space: 
        is_pixel_checking = not is_pixel_checking
        if is_pixel_checking:
            print("Pixel checking started.")
        else:
            print("Pixel checking stopped.")

    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    while listener.running:
        if is_pixel_checking:
            check_and_click_pixels()
