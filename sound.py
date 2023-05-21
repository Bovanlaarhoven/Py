import subprocess

def play_sound():
    subprocess.run(['afplay', '/System/Library/Sounds/Glass.aiff'])

play_sound()
