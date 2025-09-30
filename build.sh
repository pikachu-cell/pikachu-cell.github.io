#!/bin/bash

WATCH_DIR="./content"
COMMAND="python3 main.py"

# Make sure inotifywait is installed
if ! command -v inotifywait >/dev/null 2>&1; then
    echo "Error: inotify-tools not installed. Install with: sudo apt install inotify-tools"
    exit 1
fi

echo "Watching $WATCH_DIR for changes..."
inotifywait -m -r -e create -e delete -e modify -e move "$WATCH_DIR" |
while read path action file; do
    echo "[$(date)] Change detected: $action on $file"
    $COMMAND "$path$file"
done
