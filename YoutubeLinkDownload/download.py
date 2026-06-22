# All logic containing yt_dlp
import yt_dlp
import os
import clipboard

os.environ["SSL_CERT_FILE"] = '' 

def download_link(link: str, is_video: bool, download_location: str):
    if not download_location or download_location == 'Select Folder':
        download_location = os.getcwd()
    download_location = os.path.abspath(download_location)
    os.makedirs(download_location, exist_ok=True)

    ydl_opts = {
        'nocheckcertificate': True,
        'no_warnings': True,
        'outtmpl': os.path.join(download_location, '%(title)s.%(ext)s'),
    }

    valid = clipboard.is_youtube_link(link)
    if not valid:
        print("Invalid YouTube link")
        return

    if not is_video:
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'}]
    else:
        ydl_opts['format'] = 'best[ext=webm]/best'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def get_video_metadata(link: str):
    ydl_opts = {
        'nocheckcertificate': True,
        'quiet': True,
        'no_warnings': True,
        'extractor_retries': 3,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(link, download=False)
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        return {'title': 'Unknown', 'error': str(e)}