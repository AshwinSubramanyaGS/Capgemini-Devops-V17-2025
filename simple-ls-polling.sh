#!/bin/bash
MONITOR_DIR="/path/to/dir"
LOG_FILE="dir_monitor.log"

previous_list=$(ls -1 "$MONITOR_DIR")

while true; do
    current_list=$(ls -1 "$MONITOR_DIR")
    
    # Find new files
    new_files=$(echo "$current_list" | grep -Fxvf <(echo "$previous_list"))
    
    if [ -n "$new_files" ]; then
        while IFS= read -r file; do
            if [ -f "$MONITOR_DIR/$file" ]; then  # Ensure it's a file, not directory
                echo "$(date): $file was created in $MONITOR_DIR" >> "$LOG_FILE"
            fi
        done <<< "$new_files"
        previous_list="$current_list"
    fi
    
    sleep 2
done