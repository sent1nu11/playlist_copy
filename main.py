import os, shutil

source_path = '/mnt/ext4_data/Music/Moby/18/Moby -  We Are All Made of Stars.mp3'
dest_path = '/media/rogerwu/MUSIC'

a_file = open("Energy_Playlist.m3u", "r")
list_of_lists = []
# for line in a_file:
# #    stripped_line = line.strip()
# #    line_list = stripped_line.split()
#     if line[0] == '/':
#         list_of_lists.append(line.strip())
#
# a_file.close()
# #
# for i in list_of_lists:
#     if i[0] == '#':
#         del i[0]

# print(list_of_lists)

slash = source_path.rfind('/')+1
print(slash)
file = source_path[slash:-1]
print(file)
