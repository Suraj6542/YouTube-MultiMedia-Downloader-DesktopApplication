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


root = ThemedTk(theme="itft1")  # ( "itft1","winxpblue","keramik", "kroc"  etc.)
root.title("YouTube Video Downloader")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

for i in range(6):  
    frame.grid_rowconfigure(i, weight=1)

for i in range(2):  
    frame.grid_columnconfigure(i, weight=1)

instructions_label = ttk.Label(frame, text="Enter the YouTube video URL:")
instructions_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")

url_entry = ttk.Entry(frame, width=50)
url_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky="ew")

format_label = ttk.Label(frame, text="Select Format:")
format_label.grid(row=2, column=0, columnspan=2, pady=(0, 5), sticky="w")

formats = ["best", "mp3", "mp4"]
format_var = tk.StringVar(root)
format_var.set(formats[0])

format_menu = ttk.Combobox(frame, textvariable=format_var, values=formats)
format_menu.grid(row=3, column=0, columnspan=2, pady=(0, 10), sticky="ew")

download_button = ttk.Button(frame, text="Download", command=download_video)
download_button.grid(row=4, column=0, columnspan=2, pady=(10, 0), sticky="ew")

status_label = ttk.Label(frame, text="", font=("Arial", 10, "italic"))
status_label.grid(row=5, column=0, columnspan=2, sticky="w")

root.update_idletasks()
root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())

root.mainloop()
