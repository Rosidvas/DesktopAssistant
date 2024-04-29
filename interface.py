import tkinter as tk
import random
from PIL import ImageTk,Image

cycle = 0
check = 1
idle_num = [1, 2, 3, 4, 5, 8]
walk_left = [ 6, 7]
walk_right = [9, 10]
computer = [11, 12, 13, 14, 15]
teleport = [100]

impath = './Animations/'
window = tk.Tk()

teleport_active = False
tele_x = 100

conversation_active = False

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight() 

# window configuration
window.config(highlightbackground='black')
window.overrideredirect(True)   
window.wm_attributes('-transparentcolor', 'lightblue')
window.wm_attributes('-topmost', True)
label = tk.Label(window, bd=0, bg='lightblue')

def set_window():
    return window 

def set_label():  
    return label

def set_status(t_active, new_x):
    global teleport_active
    global tele_x

    teleport_active = t_active
    tele_x = new_x
    

def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        print(cycle)
        cycle += 1
        print(cycle)
    else:        
        cycle = 0
        event_number = random.randrange(first_num, last_num+1, 1)
    return cycle, event_number
   
   
#Start teleporter animation 
def teleport_animation(label, window, screen_height, tele_start_frames, x):
    global cycle
    global event_number
    
    y = (screen_height - window.winfo_reqheight())
    
    
    cycle = 0
    event_number = 100  # Adjust event number for teleportation animation
    update_cycle = 0
    
    # Play teleportation animation until completion
    while update_cycle < len(tele_start_frames):
        frame = tele_start_frames[update_cycle]
        window.geometry(f'300x400+{x}+{y - 48}')
        label.configure(image=frame)
        window.update_idletasks()
        window.after(100)  # Adjust delay as needed
        update_cycle += 1

    print("Teleportation complete") 


# Update to gif
def update(cycle, check, event_number, x, x_left_edge, x_right_edge):
    global frame
    global teleport_active
    global tele_x
    
    
    if teleport_active:
        x = tele_x
        teleport_animation(label, window, screen_height, tele_start_frames, x)
        teleport_active = False
    
    
    y = (screen_height - window.winfo_reqheight())

    if check == 0:
        
        frame = idle_frames[cycle]
        cycle, event_number = gif_work(cycle, idle_frames, event_number, 1, 15)
    elif check == 1 and x > -100:
        frame = walk_left_frames[cycle]
        cycle, event_number = gif_work(cycle, walk_left_frames, event_number, 1, 15)
        x -= 50
    elif check == 2 and x < screen_width - window.winfo_reqwidth() - 200:
        frame = walk_right_frames[cycle]
        cycle, event_number = gif_work(cycle, walk_right_frames, event_number, 1, 15)
        x += 50
    elif check == 3:
        frame = computer_frames[cycle]
        cycle, event_number = gif_work(cycle, computer_frames, event_number, 1, 15)
    elif check == 100: #Teleportation
        frame = tele_start_frames[cycle]
        cycle, event_number = gif_work(cycle, tele_start_frames, event_number, 1, 15)
        print("Cycle:", cycle)
        print("Length of teleport_frames:", len(computer_frames))
        print("The teleport was active!")
        print(len(tele_start_frames))
    else:
        event_number = random.randrange(1, 15, 1)
        print("skipped")

    #print(x)
    window.geometry(f'300x400+{x}+{y- 48}')
    label.configure(image=frame)
    window.after(1,event,cycle,check,event_number,x, x_left_edge, x_right_edge)

#switch gifs based on number
def event(cycle, check, event_number, x, x_left_edge, x_right_edge):
    
    if event_number in idle_num:
        check = 0
        window.after(500, update, cycle, check, event_number, x, x_left_edge, x_right_edge)  # no. 1,2,3,4 = idle
    elif event_number in walk_left:
        check = 1
        window.after(200, update, cycle, check, event_number, x, x_left_edge, x_right_edge)  # no. 6,7 = walk towards left
    elif event_number in walk_right:
        check = 2
        window.after(200, update, cycle, check, event_number, x, x_left_edge, x_right_edge)  # no 8,9 = walk towards right
    elif event_number in computer:
        check = 3
        window.after(2000, update, cycle, check, event_number, x, x_left_edge, x_right_edge)
    elif event_number == 100:
        window.after(1000, update, cycle, check, event_number, x, x_left_edge, x_right_edge)


# frames
idle_frames = [tk.PhotoImage(file=impath + 'sonic_idle_2.gif', format='gif -index %i' % (i)) for i in range(2)]
walk_right_frames = [tk.PhotoImage(file=impath + 'sonic_run_right.gif', format='gif -index %i' % (i)) for i in range(4)]
walk_left_frames = [tk.PhotoImage(file=impath + 'sonic_run_left.gif', format='gif -index %i' % (i)) for i in range(4)]
computer_frames = [tk.PhotoImage(file=impath + 'sonic_idle_2.gif', format='gif -index %i' % (i)) for i in range(2)]
tele_start_frames = [tk.PhotoImage(file=impath + 'sonic_teleport.gif', format='gif -index %i' % (i)) for i in range(12)]

