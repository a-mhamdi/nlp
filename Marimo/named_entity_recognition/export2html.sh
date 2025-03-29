#!/bin/bash

FILENAMES=$( ls | grep -E ".py$" | awk '{split($0, filename, ".py"); print filename[1]}' )

for filename in $FILENAMES
do
	echo "Processing $filename.py"
	../../.venv/bin/python -m marimo export html $filename".py" -o $filename".html"
done;

read -n 1 -s -p "Press space to delete html files..."

ls | grep -E ".html$" | xargs rm 

