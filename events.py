import tkinter as tk
import random
from interface import set_window, set_status
# from voice_v2 import on_press, on_release

window = set_window()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

##Teleport event
def onclick_teleport(Event):
    print("teleport active")
    new_x_after_teleport = generate_x_coordinate(window, screen_width) #x + 200
    teleport_active = True

    set_status(teleport_active, new_x_after_teleport)

def generate_x_coordinate(window, screen_width, exclusion_range=200):
    while True:
        number = random.randint(-200, screen_width)
        if not (window.winfo_x() - 200 <= number <= window.winfo_x() + 200):
            return number


