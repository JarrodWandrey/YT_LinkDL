# All logic regarding tkinter UI
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style, Progressbar
from functools import partial

def CreateWindow():
    window = Tk()
    window.geometry('500x250+1000+300')
    window.update()
    window.title("New Link Detected")
    label_frame = LabelFrame(window, text=('Download youtube link?'),background="grey")
    label_frame.pack(expand = 'yes', fill = 'both')
    btn1 = Button(label_frame, text = 'WEBM Download')
    btn1.place(x=100,y=150)
    btn2 = Button(label_frame, text= 'MP3 Download')
    btn2.place(x=300, y=150)
    btn3 = Button(label_frame, text = 'Exit', command= window.destroy)
    btn3.place(x=450, y=0)
    dlbar = Progressbar(label_frame, orient= HORIZONTAL, length= 400, mode= "determinate")
    dlbar.place(x=50, y=100)
    videotitle = Label(window, text="Video Title", font=20,background="grey")
    videotitle.place(x=90, y=50)
    window.mainloop()