#!/usr/bin/env python3
'''
    This is a proof of concept script.
    This file is published under the wtfpl.net license
'''
'''
    Expected output:
    {
      "name": "Mainsail OS 1.2.1 32-Bit (recommend)",
      "description": "Type: raspberry, SBC: rpi32",
      "url": "https://github.com/mainsail-crew/MainsailOS/releases/download/1.2.1/2023-05-26-MainsailOS-1.2.1-raspberry-rpi32.img.xz",
      "icon": "https://os.mainsail.xyz/rpi-imager.png",
      "init_format": "systemd",
      "release_date": "2023-05-26",
      "extract_size": 6253708288,
      "extract_sha256": "83f26b37ab04a459a22fb2121d8d6aed5cb92d4a15b86dda08d6a8ecd381748b",
      "image_download_size": 1135938556,
      "image_download_sha256": "508b20cdbb438d37f9cbb01d345e6f9f92f4cd8b22ba70889f658526cd60584c"
    },
'''

'''
    Available git action variables/outputs
    name: "Mainsail OS ${{ github.event.inputs.version }}"
    description: "Type: ${{ steps.build.outputs.type }}, SBC: ${{ steps.build.outputs.sbc }}"
    type: "${{ steps.build.outputs.type }}"
    sbc: "${{ steps.build.outputs.sbc }}"
    url: "https://github.com/mainsail-crew/MainsailOS/releases/download/${{ github.event.inputs.version }}/${{ steps.move-image.outputs.image }}.img.xz"
    icon: "https://os.mainsail.xyz/rpi-imager.png"
    init_format: "systemd"
    release_date: "${{ needs.release.outputs.date }}"
    extract_size: ${{ steps.filesizes.outputs.image }}
    extract_sha256: "${{ steps.checksums.outputs.image }}"
    image_download_size: ${{ steps.filesizes.outputs.zip }}
    image_download_sha256: "${{ steps.checksums.outputs.zip }}"
'''

import json

base_url = "https://github.com/mainsail-crew/MainsailOS/releases/download/"
image = "2023-05-26-MainsailOS-1.2.1-raspberry-rpi32" # ${{ steps.move-image.outputs.image }}
description = "A port of Raspberry Pi OS with basic components to run Mainsail"
icon = "https://os.mainsail.xyz/rpi-imager.png"

# Read config for SUPPORTED_SBC
with open('./config', 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('SUPPORTED_SBC'):
            line = line.replace('SUPPORTED_SBC=', '')
            line = line.replace('"', '')
            sbcs = line.split()

# Get os_type = 32bit / 64bit
sbc = "rpi32" # ${{ steps.build.outputs.sbc }}
if "rpi32" in sbc:
    os_type = "(32-bit)"
elif "rpi64" in sbc:
    os_type = "(64-bit)"

# Get version
version = "1.2.1" # ${{ github.event.inputs.version }}

# Concatenate name
name = f'Mainsail OS {version} {os_type}'

# Construct url
url = f'{base_url}{version}/{image}.img.xz'

# Get release date
release_date = "2023-05-26" # ${{ needs.release.outputs.date }}

# file sizes
extract_size = 6253708288 # ${{ steps.filesizes.outputs.image }}
image_download_size = 1135938556 # ${{ steps.filesizes.outputs.zip }}

# checksums
# ${{ steps.checksums.outputs.image }}
extract_sha256 = "83f26b37ab04a459a22fb2121d8d6aed5cb92d4a15b86dda08d6a8ecd381748b"
# ${{ steps.checksums.outputs.zip }}
image_download_sha256 = "508b20cdbb438d37f9cbb01d345e6f9f92f4cd8b22ba70889f658526cd60584c"

# Init dict
data = {}
# construct dict
data.update({"name": name})
data.update({"description": description})
data.update({"url": url})
data.update({"icon": icon})
data.update({"init_format": "systemd"})
data.update({"release_date": release_date})
data.update({"extract_size": extract_size})
data.update({"extract_sha256": extract_sha256})
data.update({"image_download_size": image_download_size})
data.update({"image_download_sha256": image_download_sha256})
data.update({"devices": sbcs})

# Convert to JSON string
data = json.dumps(data)

# Write to file ${{ steps.move-image.outputs.image }}
output_file = "./{}.json".format(image)

with open(output_file, "w") as json_file:
    json_file.write(data)
