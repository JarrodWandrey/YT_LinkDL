# Logic for detecting clipboard contents and validation
import pyperclip
import time
import download, gui

def start_watching():
    previous_clipboard = ""
    while True:
        current_clipboard = pyperclip.paste()
        if current_clipboard != previous_clipboard and is_youtube_link(current_clipboard):
            # Process the new link
            video_metadata = download.get_video_metadata(current_clipboard)
            handle_new_link(video_metadata['title'])
            previous_clipboard = current_clipboard

        time.sleep(1)  # Check clipboard every second

# Looking online there is a crazy regex way to validate youtube links
# Might look into that later, for now just check if the string contains "youtube.com"
def is_youtube_link(link:str) -> bool:
    return "youtube.com" in link.lower()

def handle_new_link(title:str):
    print(f"New YouTube link detected: {title}")
    gui.PopupWindow(title)