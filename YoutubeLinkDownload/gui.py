# All logic regarding tkinter UI
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style, Progressbar
from functools import partial
import download

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
    video_label = ttk.Label(main_frame, text="Will have to think of something", font=("Segoe UI", 10))
    video_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    # Progress bar
    dlbar = ttk.Progressbar(main_frame, orient=HORIZONTAL, length=400, mode="determinate")
    dlbar.grid(row=2, column=0, columnspan=2, pady=10)

    # Buttons frame
    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=3, column=0, columnspan=2, pady=10)

    btn1 = ttk.Button(button_frame, text='Download WEBM', command=partial(download.download_link, is_video=True))
    btn1.grid(row=0, column=0, padx=10)

    btn2 = ttk.Button(button_frame, text='Download MP3', command=partial(download.download_link, is_video=False))
    btn2.grid(row=0, column=1, padx=10)

    # Exit button
    exit_btn = ttk.Button(main_frame, text="Exit", command=window.destroy)
    exit_btn.grid(row=4, column=1, sticky="e", pady=5)

    window.mainloop()

def PopupWindow(title):
    # Small window when running headless
    popup = Tk()
    popup.geometry('400x175')
    popup.title("New Link Detected")

    # Main frame
    main_frame = ttk.Frame(popup, padding=15)
    main_frame.pack(fill="both", expand=True)

    # Title label
    title_label = ttk.Label(main_frame, text="Download YouTube Link?", font=("Segoe UI", 14, "bold"))
    title_label.pack(pady=(0,5))

    # Video title
    video_label = ttk.Label(main_frame, text=title, font=("Segoe UI", 10))
    video_label.pack(pady=(0, 10))
    
    # Buttons frame
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=5)

    btn1 = ttk.Button(button_frame, text='Download WEBM', command=partial(download.download_link, is_video=True))
    btn1.pack(side="left", padx=5)

    btn2 = ttk.Button(button_frame, text='Download MP3', command=partial(download.download_link, is_video=False))
    btn2.pack(side="left", padx=5)

    # Exit button
    exit_btn = ttk.Button(main_frame, text="Exit", command=popup.destroy)
    exit_btn.pack(pady=5)

    popup.mainloop()