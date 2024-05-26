# YouTube to MP3 Downloader and Metadata Updater

This Python script provides a GUI application to download YouTube videos as MP3 files and update their metadata automatically. It utilizes the MusicBrainz API to fetch song details for the downloaded MP3 files.

## Prerequisites

Ensure you have the following dependencies installed:

- Python 3.x
- Tkinter (https://docs.python.org/3/library/tkinter.html)
- Mutagen(https://mutagen.readthedocs.io/en/latest/)
- MusicBrainzNGS(https://python-musicbrainzngs.readthedocs.io/en/v0.7.1/)
  
  (Ffmpeg and yt-dlp are already locally installed in the file)
  
## Usage

1. Run the script `youtune.py`.
2. Enter the YouTube URL of the video you want to download.
3. Choose the output folder where you want to save the downloaded MP3 files.
4. Click the "Start" button to initiate the download and metadata update process.


## Notes

- This script assumes that the YouTube video contains music and uses MusicBrainz to fetch metadata based on the song title.
- The GUI is built using Tkinter, a standard GUI toolkit for Python.

Feel free to contribute to the project by submitting issues or pull requests!

