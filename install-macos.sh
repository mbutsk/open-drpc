#!/bin/bash

# Superuser check
if [ "$EUID" -eq 0 ]; then
    echo "Run the script as a user (not superuser)"
    exit 1
fi

# Variables
AGENT_NAME="open-drpc"
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAUNCHD_PLIST_PATH="$HOME/Library/LaunchAgents/$AGENT_NAME.plist"
SHARE_PATH="$HOME/.local/share/open-drpc"

# Venv
python3 -m venv "$SHARE_PATH/venv"
"$SHARE_PATH/venv/bin/pip" install -r "$SCRIPT_PATH/requirements.txt"

# Create LaunchAgent plist
mkdir -p "$(dirname "$LAUNCHD_PLIST_PATH")"

cat <<EOF > "$LAUNCHD_PLIST_PATH"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$AGENT_NAME</string>

    <key>ProgramArguments</key>
    <array>
        <string>$SHARE_PATH/venv/bin/python</string>
        <string>$SCRIPT_PATH/open-drpc/main.py</string>
    </array>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
EOF

# Start Agent
launchctl load "$LAUNCHD_PLIST_PATH"
launchctl start "$AGENT_NAME"
