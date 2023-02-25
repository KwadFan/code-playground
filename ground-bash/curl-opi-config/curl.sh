#!/bin/bash

BASE_URL="https://raw.githubusercontent.com/orangepi-xunlong/orangepi-build/next/external/cache/sources/orangepi-config/"
FILES="debian-config debian-config-functions debian-config-functions-network debian-config-jobs debian-config-submenu"
TMP="./tmp"

rm -f "${TMP}"/*

create_array() {
    for i in ${FILES}; do
        FILES_ARRAY+=("${i}")
    done
}

create_array

for file in "${FILES_ARRAY[@]}"; do
    curl -sL "${BASE_URL}"/"${file}" --output "${TMP}"/"${file}"
done


#echo "${FILES[@]:1}"

for i in "${FILES_ARRAY[@]:1}"; do
    stripped="${i##debian-config-}"
    echo "${stripped}.sh"
    cp -f "${TMP}/${i}" "./usr/lib/orangepi-config/${stripped}.sh"
done

cp -f "${TMP}"/"${FILES_ARRAY[*]:0:1}" "./usr/sbin/orangepi-config"
