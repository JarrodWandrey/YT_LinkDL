from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style, Progressbar
from functools import partial
import yt_dlp
import time

downloads = [] #list to store all previously downloaded youtube links
fullstring = ''
class DownloadWindow:
    donedownloading = False
    def createWindow(self):
        self.window = window = Tk()
        window.geometry('500x250+1000+300')
        window.update()
        window.title("New Link Detected")
        label_frame = LabelFrame(window, text=('Download youtube link?'))
        label_frame.pack(expand = 'yes', fill = 'both')
        btn1 = Button(label_frame, text = 'WEBM Download', command= partial(self.downloadlink, True))
        btn1.place(x=100,y=150)
        btn2 = Button(label_frame, text= 'MP3 Download', command= partial(self.downloadlink, False))
        btn2.place(x=300, y=150)
        btn3 = Button(label_frame, text = 'Exit', command= window.destroy)
        btn3.place(x=450, y=0)
        with yt_dlp.YoutubeDL() as ydl:
            videoLink = ydl.extract_info(fullstring,download=False)
        self.dlbar = dlbar = Progressbar(label_frame, orient= HORIZONTAL, length= 400, mode= "determinate")
        dlbar.place(x=50, y=100)
        video_url = Label(self.window, text=fullstring)
        video_url.place(x=100, y=75)
        videotitle = Label(self.window, text=videoLink['title'])
        videotitle.place(x=100, y=20)
        window.mainloop()

    def downloadlink(self, isVideo):
        ydl_opts = {
            'format': 'bestaudio/best',
            'progress_hooks': [self.Progress],
            } #Formatting the downloaded YouTube Link
        if not isVideo: #loop for downloading the WEBM
            ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'}]
        label = LabelFrame(self.window, text=('Downloading.'))
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("New Youtube link detected.")
            ydl.download([fullstring])
        downloads.append(fullstring) #Adds new youtube link to list so no double downloads happen

    def Progress(self, data): #progress bar function
        if self.donedownloading or data["status"] == "error":
            return
        pcomplete = (data["downloaded_bytes"] / data["total_bytes"])*100 #calculation for completed progress shown on bar
        print(f"\n{pcomplete}")
        self.dlbar['value'] = pcomplete
        self.window.update_idletasks()
        if pcomplete == 100: #Close the window when download is finished
            self.donedownloading = True
            self.window.destroy()

while True:
    time.sleep(3)
    clipboardwindow = Tk()
    fullstring = clipboardwindow.clipboard_get() #Grab Full value form clipboard
    clipboardwindow.withdraw()
    substring = "youtube.com" #Substring to filter clipboards value to be a youtube link
    if substring in fullstring.lower() and fullstring not in downloads: #If clipboard value contains the substring AND if the fullstring link is not already been downloaded cont
        NewWindow = DownloadWindow()
        NewWindow.createWindow()

