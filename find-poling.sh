#!/bin/bash
MONITOR_DIR="/path/to/dir"
LOG_FILE="dir_monitor.log"

# Get initial state
previous_files=$(find "$MONITOR_DIR" -maxdepth 1 -type f -printf "%f\n" | sort)

while true; do
    # Get current state
    current_files=$(find "$MONITOR_DIR" -maxdepth 1 -type f -printf "%f\n" | sort)
    
    # Find new files (created)
    new_files=$(comm -13 <(echo "$previous_files") <(echo "$current_files"))
    
    if [ -n "$new_files" ]; then
        for file in $new_files; do
            echo "$(date): $file was created in $MONITOR_DIR" >> "$LOG_FILE"
        done
        previous_files="$current_files"
    fi
    
    sleep 5  # Check every 5 seconds
done