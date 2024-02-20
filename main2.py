import random
import tkinter as tk
import pyautogui
from functools import partial
from pathlib import Path

global x 
x = 1400
cycle = 0
check = 1
idle_num = [1, 2, 3, 4, 5, 8]
walk_left = [ 6, 7]
walk_right = [9, 10]
teleport = [11]
event_number = random.randrange(1, 3, 1)
impath = './Animations/'


# Loops the gifs
def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:        
        cycle = 0
        event_number = random.randrange(1, 11, 1)
    return cycle, event_number

   
# Update to gif
def update(cycle, check, event_number, x, x_left_edge, x_right_edge):
    global frame
    y = (screen_height - window.winfo_reqheight())

    if check == 0:
        frame = idle_frames[cycle]
        cycle, event_number = gif_work(cycle, idle_frames, event_number, 1, 3)
    elif check == 1 and x > -100:
        frame = walk_left_frames[cycle]
        cycle, event_number = gif_work(cycle, walk_left_frames, event_number, 1, 3)
        x -= 50
    elif check == 2 and x < screen_width - window.winfo_reqwidth() - 200:
        frame = walk_right_frames[cycle]
        cycle, event_number = gif_work(cycle, walk_right_frames, event_number, 1, 3)
        x += 50
    elif check == 11:
        frame = walk_right_frames[cycle]
        cycle, event_number = gif_work(cycle, walk_right_frames, event_number, 1, 3)
        x += 100
    else:
        event_number = random.randrange(1, 11, 1)
        print("skipped")

    print(x)
    window.geometry(f'+{x}+{y}')
    label.configure(image=frame)
    window.after(1,event,cycle,check,event_number,x, x_left_edge, x_right_edge)


def event(cycle, check, event_number, x, x_left_edge, x_right_edge):
    

    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(2000, update, cycle, check, event_number, x, x_left_edge, x_right_edge)  # no. 1,2,3,4 = idle
    elif event_number in walk_left:
        check = 1
        print('walking towards left')
        window.after(200, update, cycle, check, event_number, x, x_left_edge, x_right_edge)  # no. 6,7 = walk towards left
    elif event_number in walk_right:
        check = 2
        print('walking towards right')
        window.after(200, update, cycle, check, event_number, x, x_left_edge, x_right_edge)  # no 8,9 = walk towards right
    elif event_number in teleport:
        check = 11
        print('teleport')
        window.after(100, update, cycle, check, event_number, x, x_left_edge, x_right_edge)


window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


# Start Window position
x_coordinate = (screen_width - window.winfo_reqwidth()) // 2
y_coordinate = (screen_height - window.winfo_reqheight()) // 2
window.geometry(f'{window.winfo_reqwidth()}x{window.winfo_reqheight()}+{x_coordinate}+{y_coordinate}')
print(window.winfo_screenwidth())
print("starting")



# Calculate the x-coordinate for screen edges
x_left_edge = (screen_width - window.winfo_reqwidth()) // 2
x_right_edge = x_left_edge + screen_width


def onclick_teleport(event):
    global x
    x = window.winfo_x()
    # event_number = 11
    print("pressed")
    if event.widget == window:
        print("fake")

    x += 200
    window.geometry(f'+{x}+{(screen_height - window.winfo_reqheight())}')
    # window.after(1, update, cycle, check, event_number, x, x_left_edge, x_right_edge)


    
        
window.bind("<Button-1>", onclick_teleport)    

# frames
idle_frames = [tk.PhotoImage(file=impath + '001_idle.gif', format='gif -index %i' % (i)) for i in range(1)]
walk_right_frames = [tk.PhotoImage(file=impath + '002_walkright.gif', format='gif -index %i' % (i)) for i in range(1)]
walk_left_frames = [tk.PhotoImage(file=impath + '003_walkleft.gif', format='gif -index %i' % (i)) for i in range(1)]


# pyautogui.displayMousePosition()

# window configuration
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black')
window.attributes('-topmost', True)
label = tk.Label(window, bd=0, bg='black')
label.pack()

window.after(1, update, cycle, check, event_number, x, x_left_edge, x_right_edge)
print("starting 2")
window.mainloop()
