#!/usr/bin/env bash

# Try to build an Ini parser in bash

# set -x

INI_FILE="./test.conf"

# echo "Print ${INI_FILE}"
# cat "${INI_FILE}"

# "Try to display sections"

# while IFS= read -r line ; do
#     #printf "%s\n" "${line}"
#     echo "${line}" | grep "^\[.*\]$"
# done < "${INI_FILE}"

# that worked but we dont want that [] thingies :)

# while IFS= read -r line ; do
#     #printf "%s\n" "${line}"
#     echo "${line}" | grep "^\[.*\]$" | sed 's/\[//g;s/\]//g'
# done < "${INI_FILE}"

# cool, worked as I wanted but that is simply not enough
# Maybe we could save some time here if we work on an cleared file
# Stripping out comments and whitespaces.

# sed '/^#/d; /^[[:space:]]*$/d' < "${INI_FILE}"

# No the file is much shorter and probably fits into an array :)

# sed '/^#/d; /^[[:space:]]*$/d' < "${INI_FILE}"

# lets put it into an array

mapfile -t file_array < <(sed '/^#/d; /^[[:space:]]*$/d; s/[[:blank:]]#.*$//' < "${INI_FILE}")

# echo "${file_array[@]}"

# Now lets print sections, maybe iterate through (might be slow)

# printf "Print sections:\n"
# for sec in "${file_array[@]}"; do
#     if grep -q "^\[.*\]$" <<< "${sec}"; then
#         # get rid of braces
#         sec="${sec/\[/}"
#         sec="${sec/\]/}"
#         echo "${sec}"
#     fi
# done

# For easier readablity by bash convert : to =

file_array=("${file_array[@]/\:/=}")
file_array=("${file_array[@]/=*[[:blank:]]/=}")


echo "${file_array[@]}"

for i in "${file_array[@]}"; do
    if [[ "$i" =~ ^\[.*\] ]]; then
        i="${i/\[/}"
        i="${i/\]/}"
        printf "%s\n" "${i}"
    fi
done

find='[testsect]'

echo ${file_array[$find]}
