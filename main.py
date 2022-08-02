import os, shutil

source_file = '/mnt/ext4_data/Music/Anastacia/Freak of Nature/Anastacia -  Paid My Dues.mp3'
destination_folder_path = '/media/rogerwu/MUSIC'
slash = '/'

playlist_file = open("Energy_Playlist.m3u", "r")
playlist_lists = []
for line in playlist_file:
#    stripped_line = line.strip()
#    line_list = stripped_line.split()
    if line[0] == '/':
        playlist_lists.append(line.strip())

playlist_file.close()

for filepath in playlist_lists:
    source_filepath = filepath
    last_slash_position = source_filepath.rfind('/') + 1
    music_file = source_filepath[last_slash_position:len(source_file)]

    destination_filepath= destination_folder_path + '/' + music_file   # ie /media/rogerwu/MUSIC
    print(f"destination_filepath: {destination_filepath}")

    shutil.copy(source_filepath, destination_filepath)

    # print(f"last_slash_position: {last_slash_position}")
    # print(f"source_filepath : {source_filepath}")
    # print(f"music_file : {music_file}")
    # print(type(destination_folderpath))
    # destination_filepath = destination_folderpath + slash + music_file
    # print(destination_filepath)

# print(playlist_lists)
# #
# lastslash_position = source_file.rfind('/')+1
# print(lastslash_position)
# music_file = source_file[lastslash_position:len(source_file]
# print("Music_file", music_file)

# dest_file = dest_path + "/" + file
