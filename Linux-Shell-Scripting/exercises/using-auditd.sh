#!/bin/bash
MONITOR_DIR="/path/to/dir"
LOG_FILE="dir_monitor.log"
AUDIT_KEY="dir_monitor"

# Setup audit rule (run as root)
sudo auditctl -w "$MONITOR_DIR" -p w -k "$AUDIT_KEY"

# Monitor audit logs continuously
sudo ausearch -k "$AUDIT_KEY" -ts today -raw | while read line; do
    if echo "$line" | grep -q "type=CREATE"; then
        file=$(echo "$line" | grep -o 'name="[^"]*"' | cut -d'"' -f2)
        echo "$(date): $(basename "$file") was created in $(dirname "$file")" >> "$LOG_FILE"
    fi
done