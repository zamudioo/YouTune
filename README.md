# YouTube to MP3 Downloader and Metadata Updater

This Python script provides a GUI application to download YouTube videos as MP3 files and update their metadata automatically. It utilizes the MusicBrainz API to fetch song details for the downloaded MP3 files.

## Prerequisites

Ensure you have the following dependencies installed:

- Python 3.x
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Mutagen](https://mutagen.readthedocs.io/en/latest/)
- [MusicBrainzNGS](https://python-musicbrainzngs.readthedocs.io/en/v0.7.1/)
- [FFmpeg](https://ffmpeg.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

Place the `ffmpeg` and `yt-dlp` binaries in the script's directory or specify their paths in the script.

Installation
You can easily install the dependencies by executing the following command in your terminal:

pip install -r requirements.txt

Make sure you have cloned or downloaded this repository to your local system before running the above command.
Run the script youtune.py.
Enter the YouTube URL of the video you want to download.
Choose the output folder where you want to save the downloaded MP3 files.
Click the "Start" button to initiate the download and metadata update process.

#Notes
This script assumes that the YouTube video contains music and uses MusicBrainz to fetch metadata based on the song title.
It utilizes yt-dlp to download YouTube videos as MP3 files and ffmpeg for audio extraction.
The GUI is built using Tkinter, a standard GUI toolkit for Python.
Feel free to contribute to the project by submitting issues or pull requests!
