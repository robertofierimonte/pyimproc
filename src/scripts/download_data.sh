#!/bin/bash
for volume in "textures" "aerials" "misc" "sequences"; do
    echo "Downloading $volume data..."
    curl -L -o "data/$volume.tar.gz" "sipi.usc.edu/database/$volume.tar.gz"
    tar -xzf "data/$volume.tar.gz" -C "data/"
    rm "data/$volume.tar.gz"
done