import os, shutil


a_file = open("Energy_Playlist.m3u", "r")
list_of_lists = []
for line in a_file:
#    stripped_line = line.strip()
#    line_list = stripped_line.split()
    if line[0] == '/':
        list_of_lists.append(line.strip())

a_file.close()
#
# for i in list_of_lists:
#     if i[0] == '#':
#         del i[0]

print(list_of_lists)
