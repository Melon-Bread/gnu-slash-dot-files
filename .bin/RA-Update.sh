#!/usr/bin/env bash

echo 'Updating RetroArch...'
yay -S retroarch-git --noconfirm

echo 'Updating Cores....'
python ~/Documents/Projects/RetroUFO/RetroUFO.py

echo 'Updating Thumbnails'
cd "~/.config/retroarch/thumbnails/"
git pull --recurse-submodules
git submodule update --remote --recursive
