import tkinter as tk
from tkinter import ttk
import yt_dlp
import os

def download_video():
    url = url_entry.get()
    selected_format = format_var.get()

    try:
        download_dir = 'C:\\Users\\hp\\Downloads'
        os.makedirs(download_dir, exist_ok=True)

        ydl_opts = {
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best' if selected_format == 'mp3' else selected_format,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }] if selected_format == 'mp3' else [],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
        
        status_label.config(text="Download completed successfully.")
    except Exception as e:
        status_label.config(text="Download failed. Check the URL and try again.")
        print(e)


root = tk.Tk()
root.title("YouTube Video Downloader")

instructions_label = tk.Label(root, text="Enter the YouTube video URL:")
instructions_label.pack()

url_entry = tk.Entry(root, width=80)
url_entry.pack()

format_label = tk.Label(root, text="Select Format:")
format_label.pack()

formats = ["best", "mp3", "mp4"]
format_var = tk.StringVar(root)
format_var.set(formats[0])

format_menu = ttk.Combobox(root, textvariable=format_var, values=formats)
format_menu.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
