import os, shutil

source_file = '/mnt/ext4_data/Music/Anastacia/Freak of Nature/Anastacia -  Paid My Dues.mp3'
destination_folder_path = '/media/rogerwu/MUSIC'
slash = '/'

playlist_file = open("Favorites.m3u", "r")
playlist_lists = []
for line in playlist_file:
    if line[0] == '/':
        playlist_lists.append(line.strip())

playlist_file.close()

for filepath in playlist_lists:
    source_filepath = filepath
    last_slash_position = source_filepath.rfind('/') + 1
    music_file = source_filepath[last_slash_position:len(source_filepath)]
    destination_filepath= destination_folder_path + '/' + music_file   # ie /media/rogerwu/MUSIC
    print(f"Copying: {destination_filepath}")

    shutil.copy(source_filepath, destination_filepath)

