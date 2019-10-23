#Daniel Pingrey
#9/27/19


import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound

h = 0
m = 0
s = 0
t = "am"

def current_time(h,m,s,t):
    totalSeconds = calendar.timegm(time.gmtime())
    currentSecond = totalSeconds%60

    totalMinutes = totalSeconds//60
    currentMinute = totalMinutes%60

    totalHours = totalMinutes//60
    currentHour = (totalHours%24)-6

    am_pm= " "
    if currentHour>= 12:
        currentHour = currentHour-12
        am_pm= "PM"
        if currentHour==0:
            currentHour=currentHour+12
    else:
        am_pm= "AM"
        if currentHour==0:
            currentHour=currentHour+12
    alarm= str(h)+":"+str(m)+":"+str(s)+t        
    timex= str(currentHour)+":"+str(currentMinute)+":"+str(currentSecond)+" "+am_pm

    if timex == alarm:
        beep()

    return timex
def beep():
    for i in range(10):
        winsound.Beep(640,5000)
    
def show_time():
    global h
    global m
    global s
    global t
    time = current_time(h,m,s,t)
    txt.set(time)
    root.after(1000, show_time)
    
def get_alarm(*args):
    global h
    h=input("What hour?: ")
    global m
    m=input("What minute?: ")
    global s
    s=input("What second?: ")
    global t
    t=input("am or pm?: ").upper()
def quit(*args):
    root.destroy()

#create root window
root = Tk()
#window size
root.geometry("550x275")
root.attributes("-fullscreen",False)
root.title("it's Time")
#set window background color
root.configure(background='Navy Blue')
#key bindings
root.bind("x", quit)
root.bind("a", get_alarm)
root.after(1000, show_time)
#font
fnt = font.Font(family='Jokerman', size=60, weight='bold')
txt=StringVar()
#display time and text color
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground="Black", background='Maroon4')
#place time in center of screen
lbl.place(relx=0.5, rely=0.5, anchor = CENTER)
#start loop
root.mainloop()

