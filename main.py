import random
import tkinter as tk
import pyautogui
from functools import partial
from pathlib import Path
from pynput import keyboard
from interface import update, set_window, set_label
from events import onclick_teleport

x = 1400
cycle = 0
check = 1
event_number = random.randrange(1, 3, 1)
  
window = set_window()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_coordinate = (screen_width - window.winfo_reqwidth()) // 2 
y_coordinate = (screen_height - window.winfo_reqheight()) // 2 + 200
window.geometry(f'{window.winfo_reqwidth()}x{window.winfo_reqheight()}+{x_coordinate}+{y_coordinate}')

# Start Window position
print(window.winfo_screenwidth())
print("starting")

# Calculate the x-coordinate for screen edges
x_left_edge = (screen_width - window.winfo_reqwidth()) // 2
x_right_edge = x_left_edge + screen_width

#handle events        
window.bind("<Button-1>", onclick_teleport)    

# pyautogui.displayMousePosition()
label = set_label()
label.pack()

window.after(1, update, cycle, check, event_number, x, x_left_edge, x_right_edge)
print("starting 2")
window.mainloop()

'''
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
'''