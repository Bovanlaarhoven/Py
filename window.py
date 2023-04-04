import tkinter as tk
import time
import sys

window = tk.Tk()

window.overrideredirect(True)

window.wm_attributes("-topmost", True)

window.geometry("150x25")

window.attributes("-alpha", 0.5)

fps_label = tk.Label(text="")
fps_label.pack()

def update_fps():
    current_time = time.time()

    fps = 1 / (current_time - update_fps.last_time)
    fps_label.config(text=f"FPS: {fps:.0f}")

    elapsed_time = time.time() - current_time
    update_interval = 1000 / 60
    wait_time = max(0, update_interval - elapsed_time)

    window.after(int(wait_time), update_fps)

    update_fps.last_time = current_time

update_fps.last_time = time.time()
update_fps()

try:
    window.mainloop()
except KeyboardInterrupt:
    window.destroy()
    sys.exit()
