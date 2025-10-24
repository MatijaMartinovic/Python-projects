import yt_dlp
import tkinter as tk
from tkinter import ttk
import os

def get_default_videos_folder():
    videos_folder = os.path.join(os.path.expanduser("~"), "Videos")
    return videos_folder

def get_video_info(url, frame):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        # show error in GUI frame and stop
        for widget in frame.winfo_children():
            widget.destroy()
        ttk.Label(frame, text="Error getting video info:", font=("Calibri", 14, "bold")).pack(pady=5)
        ttk.Label(frame, text=str(e), font=("Calibri", 12)).pack(pady=5)
        return

    info = {
        "title": info.get('title'), # type: ignore
        "author": info.get('uploader'), # type: ignore
        "views": info.get('view_count'), # type: ignore
        "Date": info.get('upload_date') # type: ignore
    }

    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="Video Information", font=("Calibri", 14, "bold")).pack(pady=5)

    for key, value in info.items():
        info_frame = ttk.Frame(frame)
        info_frame.pack(fill='x', padx=5, pady=2)

        ttk.Label(info_frame, text=f"{key.capitalize()}:", width=10, anchor='e', font=("Calibri", 12, "bold")).pack(side='left')
        ttk.Label(info_frame, text=value, anchor='w', font=("Calibri", 12)).pack(side='left', fill='x', expand=True) # type: ignore

    ttk.Label(frame, text="Finished fetching info!", font=("Calibri", 16, "bold")).pack()


def clear_textbox(entry):
    entry.delete(0, tk.END)


def download_video(entry, frame):
    url = entry.get()
    print(url)
    print(f"Downloading from {url}")
    ydl_opts = {
        'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(get_default_videos_folder(), "%(title)s.%(ext)s"),
        'postprocessors': [
            {'key': 'FFmpegMetadata'},
            {'key': 'EmbedThumbnail'}
        ],
        # use raw string for windows path or ensure correct escaping
        'ffmpeg_location': r'C:\Users\matij\OneDrive\Documents\ffmpeg-2025-08-04-git-9a32b86307-essentials_build\bin\ffmpeg.exe'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print("Download error:", e)
        for widget in frame.winfo_children():
            widget.destroy()
        ttk.Label(frame, text="Download error:", font=("Calibri", 14, "bold")).pack(pady=5)
        ttk.Label(frame, text=str(e), font=("Calibri", 12)).pack(pady=5)
        return

    print("Downloaded!")
    clear_textbox(entry)
    print("Finished Downloading")
    get_video_info(url, frame)
    



def on_click():
    print("hello")

def main():
    root = tk.Tk()
    root.title("YouTube Downloader")
    root.geometry("1280x720")
    root.resizable(False, False)

    title = tk.Label(root, text="Youtube Downloader")
    title.pack(pady=10)
    title.configure(font=("Calibri", 32))

    entryTx = tk.Label(root, text="Enter YouTube video link below:", font=("Calibri", 24))
    entryTx.pack(pady=10)

    entry = tk.Entry(root, width=30, font=("Calibri", 16))
    entry.pack(pady=20)
    url = entry.get()

    button = tk.Button(root, text="Download", font=("Calibri", 16), command=lambda: download_video(entry, frame))
    button.pack(pady=10)

    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)
    
    row = 0
    

    root.mainloop()

if __name__ == '__main__':
    main()