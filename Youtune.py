import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import musicbrainzngs

# Ubicación de ffmpeg y yt-dlp
ffmpeg_location = "./ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe"
yt_dlp_location = "./yt-dlp.exe"  # Asegúrate de que esta ruta sea correcta

def set_musicbrainz_credentials(username, email):
    musicbrainzngs.set_useragent("yt-to-mp3-app", "0.1", email)
    musicbrainzngs.auth(username, "")

def get_song_details(song_title):
    try:
        result = musicbrainzngs.search_recordings(recording=song_title, limit=5)
        if result['recording-list']:
            options = []
            for recording in result['recording-list']:
                title = recording['title']
                artist = recording['artist-credit'][0]['name']
                album = recording['release-list'][0]['title'] if 'release-list' in recording and recording['release-list'] else "Unknown Album"
                options.append({'title': title, 'artist': artist, 'album': album})
            return options
        else:
            return None
    except Exception as e:
        print(f"Error fetching details for {song_title}: {e}")
        return None

def update_mp3_metadata(file_path, song_details):
    try:
        audio = MP3(file_path, ID3=EasyID3)
        audio['title'] = song_details['title']
        audio['artist'] = song_details['artist']
        audio['album'] = song_details['album']
        audio.save()
        print(f"Updated metadata for {file_path}")
    except Exception as e:
        print(f"Error updating metadata for {file_path}: {e}")

def process_mp3_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            song_title = os.path.splitext(filename)[0]
            song_details = get_song_details(song_title)
            if song_details:
                chosen_details = choose_song_details(song_title, song_details)
                if chosen_details:
                    update_mp3_metadata(file_path, chosen_details)
                else:
                    print(f"No details chosen for {song_title}")
            else:
                print(f"No details found for {song_title}")

def choose_song_details(song_title, options):
    def on_select(event):
        selected_index = listbox.curselection()
        if selected_index:
            selected_option.set(selected_index[0])

    dialog = tk.Toplevel(root)
    dialog.title(f"Choose details for {song_title}")

    tk.Label(dialog, text="Choose the correct song details:").pack(pady=10)

    listbox = tk.Listbox(dialog, width=80, height=10)
    for option in options:
        listbox.insert(tk.END, f"Title: {option['title']}, Artist: {option['artist']}, Album: {option['album']}")
    listbox.pack(pady=10)

    selected_option = tk.IntVar()
    listbox.bind("<<ListboxSelect>>", on_select)

    def on_confirm():
        dialog.destroy()

    confirm_button = tk.Button(dialog, text="Confirm", command=on_confirm)
    confirm_button.pack(pady=10)

    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)

    selected_index = selected_option.get()
    return options[selected_index] if selected_index is not None and selected_index < len(options) else None

def download_youtube_video(url, output_dir):
    if not os.path.exists(yt_dlp_location):
        messagebox.showerror("Error", f"yt-dlp.exe not found at {yt_dlp_location}")
        return
    try:
        subprocess.run([
            yt_dlp_location,
            '--extract-audio',
            '--audio-format', 'mp3',
            '--ffmpeg-location', ffmpeg_location,
            '-o', os.path.join(output_dir, '%(title)s.%(ext)s'),
            url
        ], check=True)
        print(f"Downloaded and converted {url}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {url}: {e}")

def start_process():
    youtube_url = url_entry.get()
    output_dir = folder_path.get()
    username = "your_musicbrainz_username"
    email = "your_email@example.com"
    if not youtube_url or not output_dir or not username or not email:
        messagebox.showerror("Error", "Please provide all required information.")
        return

    set_musicbrainz_credentials(username, email)
    download_youtube_video(youtube_url, output_dir)
    process_mp3_files(output_dir)
    messagebox.showinfo("Success", "Download and metadata update complete.")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

root = tk.Tk()
root.title("YouTube to MP3 Downloader and Metadata Updater")

tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Output Folder:").grid(row=1, column=0, padx=10, pady=10)
folder_path = tk.StringVar()
folder_entry = tk.Entry(root, textvariable=folder_path, width=50)
folder_entry.grid(row=1, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=1, column=2, padx=10, pady=10)

start_button = tk.Button(root, text="Start", command=start_process)
start_button.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
