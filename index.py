from pytube import YouTube, Playlist

from os import path, rename

type_download = input('1_ One Music \n2_ Playlist \n')

if int(type_download) == 1:    
    url_music = input('Input URL music: ')


    print(url_music)

    yt = YouTube(url_music)

    out_file = yt.streams.filter(only_audio=True).desc().first().download(output_path='musics')

    base, ext = path.splitext(out_file)

    new_file = base + '.mp3'

    rename(out_file, new_file)

if int(type_download) == 2:
    url_playlist = input('Input URL playlist: ')
    playlist = Playlist(url_playlist)
    print(playlist)
    print(f'Downloading: {playlist.title}')
    for video in playlist.videos:
        out_file = video.streams.filter(only_audio=True).desc().first().download(output_path='musics')
        print(out_file)
        base, ext = path.splitext(out_file)
        new_file = base + '.mp3'
        rename(out_file, new_file)
