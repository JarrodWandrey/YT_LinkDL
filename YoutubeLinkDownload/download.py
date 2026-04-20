# All logic containing yt_dlp
import yt_dlp
import os

os.environ["SSL_CERT_FILE"] = ''

def download_link(link, is_video):
    ydl_opts = {
        'format': 'bestaudio/best',
        'nocheckcertificate': True,
        'no_warnings': True,
    }

    if not is_video:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'}]
    else:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'webm'}]
            
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def get_video_metadata(link):
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