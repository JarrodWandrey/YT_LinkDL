# All logic containing yt_dlp
import yt_dlp

def download_link(link, is_video):
    ydl_opts = {
        'format': 'bestaudio/best',
        'progress_hooks': [self.Progress]
    }

    if not is_video:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'}]
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

def Progress(self, data):
    if self.donedownloading or data["status"] == "error":
        return
    pcomplete = (data["downloaded_bytes"] / data["total_bytes"])*100 #calculation for completed progress shown on bar
    print(f"\n{pcomplete}")
    self.dlbar['value'] = pcomplete
    self.window.update_idletasks()
    if pcomplete == 100: #Close the window when download is finished
        self.donedownloading = True
        self.window.destroy()