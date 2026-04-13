# All logic regarding tkinter UI
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style, Progressbar
from functools import partial

def CreateWindow():
    window = Tk()
    window.geometry('500x250')
    window.title("New Link Detected")

    # Main frame
    main_frame = ttk.Frame(window, padding=15)
    main_frame.pack(fill="both", expand=True)

    # Title label
    title_label = ttk.Label(main_frame, text="Download YouTube Link?", font=("Segoe UI", 14, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Video title
    video_label = ttk.Label(main_frame, text="Video Title", font=("Segoe UI", 10))
    video_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    # Progress bar
    dlbar = ttk.Progressbar(main_frame, orient=HORIZONTAL, length=400, mode="determinate")
    dlbar.grid(row=2, column=0, columnspan=2, pady=10)

    # Buttons frame
    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=3, column=0, columnspan=2, pady=10)

    btn1 = ttk.Button(button_frame, text='Download WEBM')
    btn1.grid(row=0, column=0, padx=10)

    btn2 = ttk.Button(button_frame, text='Download MP3')
    btn2.grid(row=0, column=1, padx=10)

    # Exit button
    exit_btn = ttk.Button(main_frame, text="Exit", command=window.destroy)
    exit_btn.grid(row=4, column=1, sticky="e", pady=5)

    window.mainloop()