import random
import tkinter as tk
from pathlib import Path

x = 1400
cycle = 0
check = 1
idle_num = [1, 2, 3, 4]
walk_left = [5, 6, 7]
walk_right = [8, 9, 10]
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
def update(cycle, check, event_number, x):
    global frame
    y = (screen_height - window.winfo_reqheight())

    if check == 0:
        frame = idle_frames[cycle]
        cycle, event_number = gif_work(cycle, idle_frames, event_number, 1, 3)
    elif check == 1:
        frame = walk_left_frames[cycle]
        cycle, event_number = gif_work(cycle, walk_left_frames, event_number, 1, 3)
        x -= 50
    elif check == 2:
        frame = walk_right_frames[cycle]
        cycle, event_number = gif_work(cycle, walk_right_frames, event_number, 1, 3)
        x += 50  
        
        #elif check == 5 or check == 4:  # if check is 4 or 5: just prints
        #print("starting walk")
    window.geometry(f'+{x}+{y}')
    label.configure(image=frame)
    window.after(1,event,cycle,check,event_number,x)


def event(cycle, check, event_number, x):
    

    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(800, update, cycle, check, event_number, x)  # no. 1,2,3,4 = idle
    elif event_number in walk_left:
        check = 1
        print('walking towards left')
        window.after(200, update, cycle, check, event_number, x)  # no. 6,7 = walk towards left
    elif event_number in walk_right:
        check = 2
        print('walking towards right')
        window.after(200, update, cycle, check, event_number, x)  # no 8,9 = walk towards right


window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Start Window position
x_coordinate = (screen_width - window.winfo_reqwidth()) // 2
y_coordinate = (screen_height - window.winfo_reqheight()) // 2
window.geometry(f'+{x_coordinate}+{y_coordinate}')
print("starting")



# frames
idle_frames = [tk.PhotoImage(file=impath + '001_idle.gif', format='gif -index %i' % (i)) for i in range(1)]
walk_right_frames = [tk.PhotoImage(file=impath + '002_walkright.gif', format='gif -index %i' % (i)) for i in range(1)]
walk_left_frames = [tk.PhotoImage(file=impath + '003_walkleft.gif', format='gif -index %i' % (i)) for i in range(1)]

# window configuration
window.config(highlightbackground='black')
# window.overrideredirect(True)
# window.wm_attributes('-transparentcolor', 'black')

label = tk.Label(window, bd=0, bg='black')
label.pack()

window.after(1, update, cycle, check, event_number, x)
print("starting 2")
window.mainloop()
