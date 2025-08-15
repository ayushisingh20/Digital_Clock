#

import tkinter as tk  # import tkinter liberary for GUI 
from time import strftime

root = tk.Tk() #create main window
root.title("Digital Clock") # set window title

def time():  # a function to update the clock 
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string) # update the label text 
    label.after(1000,time) #1000ms = 1 sec # rerun after 1 sec


label = tk.Label (root,font=('calibri',50,'bold'),background='yellow',foreground='black')
label.pack(anchor ='center')

time()

root.mainloop() #keep the window open and running