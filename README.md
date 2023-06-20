# Download NewPipe Backups

This repo can be used to download backups from NewPipe as m4a files.

---

## Prerequisites

On Ubuntu 22.04, run the following to get all the prerequisites:

```
sudo apt update
sudo apt install python3 unzip sqlite3
git clone git@github.com:ytdl-org/youtube-dl.git
mv youtube-dl/youtube_dl ~/.local/lib/python*/
```

## Run

1. Transfer newpipe.zip (your backup) into the repo directory

2. Extract cookies.txt using [https://github.com/kairi003/Get-cookies.txt-LOCALLY](this), and put it in the repo directory

3. Run: `python3 download.py` - this will download all your playlists to `$REPO_DIR/playlists/$PLAYLIST_NAME/$SONG_NAME.m4a`

