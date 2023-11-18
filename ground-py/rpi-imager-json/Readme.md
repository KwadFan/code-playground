# What is this about?

Well, for a project that I am working on, I need to generate a JSON file.
this file has to contain informations about an OS image.

These are:

-   name
-   description
-   type
-   sbc
-   url
-   icon
-   init_format
-   release_date
-   extract_size
-   extract_sha256
-   image_download_size
-   image_download_sha256

Some of them are static:

-   description
-   icon
-   init_format

In the end we need that file to be listed in `rpi-imager`.

How this JSON file is structured can be viewed here:

https://downloads.raspberrypi.org/os_list_imagingutility_v4.json

The data that we provide till now looks like this:

https://os.mainsail.xyz/rpi-imager.json

```JSON
{
  "os_list": [
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
    {
      "name": "Mainsail OS 1.2.1 64-Bit",
      "description": "Type: raspberry, SBC: rpi64",
      "url": "https://github.com/mainsail-crew/MainsailOS/releases/download/1.2.1/2023-05-26-MainsailOS-1.2.1-raspberry-rpi64.img.xz",
      "icon": "https://os.mainsail.xyz/rpi-imager.png",
      "init_format": "systemd",
      "release_date": "2023-05-26",
      "extract_size": 6484395008,
      "extract_sha256": "4e0d49431bc8a632fc65caebdd0bdb8ec71de1a3408b62c4d056a3f9c247edc8",
      "image_download_size": 1064845892,
      "image_download_sha256": "fa6c219b62ed44594342c55f8efaea116dbe3bb40132275f61130dcba65c8987"
    }
  ]
}
```

This has to be generated in a github workflow, so they use github environment vars or outputs of "steps"

Now. we need to extend this with an new type `devices:`

As an Example we use JSON from Raspberry Pi OS (64-bit):

```JSON
"os_list": [
    {
      "name": "Raspberry Pi OS (64-bit)",
      "description": "A port of Debian Bookworm with the Raspberry Pi Desktop (Recommended)",
      "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
      "url": "https://downloads.raspberrypi.com/raspios_arm64/images/raspios_arm64-2023-10-10/2023-10-10-raspios-bookworm-arm64.img.xz",
      "extract_size": 5800722432,
      "extract_sha256": "f5236272f5fe2a0e3999c8c0a574772684d3bfd18f395304292ddf59508d5ae1",
      "image_download_size": 1146559440,
      "release_date": "2023-10-10",
      "init_format": "systemd",
      "devices": [
        "pi5-64bit",
        "pi4-64bit"
      ]
    },
```

So, as we now knew, how this has to look like, something to mention.

Our `devices` list comes out of a bash style script as a bash Variable.

`SUPPORTED_SBC` -> `SUPPORTED_SBC="pi1-32bit pi2-32bit pi3-32bit"`

Also, there are probably multiple Images or types, therefore we have to
concatenate two or more files (two for now).

This is the proof of concept for this task...

Tasks:

-   Read from `config`, extract `SUPPORTED_SBC`
-   Store output to variable
