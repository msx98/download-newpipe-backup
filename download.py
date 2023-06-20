#/usr/bin/env python3

import os
import time
import youtube_dl

os.system("""unzip newpipe.zip; sqlite3 newpipe.db "select playlists.name,streams.title, streams.url from playlist_stream_join inner join playlists on playlists.uid=playlist_stream_join.playlist_id join streams on streams.uid=playlist_stream_join.stream_id" -csv > playlists.csv""")
s = None
with open("playlists.csv", "r") as f:
    s = [x.split(",") for x in f.read().split("\n") if x]

playlists = dict()

for i in range(len(s)):
    playlist = s[i][0]
    if playlist.startswith("'") or playlist.startswith("\""):
        playlist = playlist[1:]
    if playlist.endswith("'") or playlist.endswith("\""):
        playlist = playlist[:-1]
    video_name = ','.join(s[i][1:-1])
    if video_name.startswith("'") or video_name.startswith("\""):
        video_name = video_name[1:]
    if video_name.endswith("'") or video_name.endswith("\""):
        video_name = video_name[:-1]
    video_url = s[i][-1]
    s[i] = (playlist, video_name, video_url)
    if playlist not in playlists:
        playlists[playlist] = dict()
    playlists[playlist][video_name] = video_url

for playlist, videos in playlists.items():
    print(f"Downloading playlist {playlist}")
    playlist_path = f"playlists/{playlist}"
    os.system(f"mkdir -p \"{playlist_path}\"")
    os.chdir(playlist_path)
    ydl_opts = {
        #"outtmpl": f"%(title)-%(id)s.%(ext)s",
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "m4a",
            "preferredquality": "192",
        }],
        "cookiefile": "cookies.txt",
    }
    for video in videos.values():
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video])
        except Exception as e:
            with open("errors.txt", "a") as f:
                f.write(f"error in {video}: {e}")
    os.chdir("../../")
