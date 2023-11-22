#!/usr/bin/env python3

'''
    Concatenate two json files and create 'os-list' JSON array.
    write to file rpi-imager.json file to finish task
'''

# Since we dont know how many files are there, lets determine first

import os
import json

# init empty file list
json_files = []

# Init os-list
os_list = []

# init data dict
data = {}

download_dir = f'{os.getcwd()}/downloads'

for file in os.listdir(download_dir):
    if file.endswith('.json'):
        file = os.path.join(download_dir, file)
        json_files.append(file)
# sort file list
json_files.sort()

# write json to dict
for json_file in json_files:
    with open(json_file, 'r') as file:
        json_string = json.load(file)
        os_list.append(json_string)



# convert dict to json
data = {"os-list": os_list}
data = json.dumps(data)

print(data)

with open('./rpi-imager.json', 'w') as rpi_json_file:
    rpi_json_file.write(data)
