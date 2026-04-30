# All logic regarding tkinter UI
from tkinter import *
from tkinter import ttk, simpledialog, filedialog
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

    #Get video title and download location in pop up window
    dialog = TwoInputDialog(window, title="YouTube Link Download")
    if dialog.result is None:
        window.destroy()
        return
    video_link, download_location = dialog.result
    video_title = download.get_video_metadata(video_link)['title']

    # Title label
    title_label = ttk.Label(main_frame, text="Download YouTube Link?", font=("Segoe UI", 14, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Video title
    video_label = ttk.Label(main_frame, text=video_title, font=("Segoe UI", 10))
    video_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    # Progress bar
    dlbar = ttk.Progressbar(main_frame, orient=HORIZONTAL, length=400, mode="determinate")
    dlbar.grid(row=2, column=0, columnspan=2, pady=10)

    # Buttons frame
    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=3, column=0, columnspan=2, pady=10)

    btn1 = ttk.Button(button_frame, text='Download WEBM', command=partial(download.download_link, link=video_link, is_video=True, download_location=download_location))
    btn1.grid(row=0, column=0, padx=10)

    btn2 = ttk.Button(button_frame, text='Download MP3', command=partial(download.download_link, link=video_link, is_video=False, download_location=download_location))
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

class TwoInputDialog(simpledialog.Dialog):
    def body(self, master):
        ttk.Label(master, text="YouTube Link:").grid(row=0)
        ttk.Label(master, text="Download Location:").grid(row=1)

        self.link_entry = ttk.Entry(master, width=20)
        self.link_entry.grid(row=0, column=1, padx=5, pady=5)

        self.location_entry = ttk.Button(master, text="Select Folder", command=self.select_folder)
        self.location_entry.grid(row=1, column=1, padx=5, pady=5)
        return self.link_entry  # initial focus
    
    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        self.location_entry.config(text=folder_selected)

    def apply(self):
        self.result = (self.link_entry.get(), self.location_entry.cget("text"))