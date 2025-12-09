#!/bin/bash

# Superuser check
if [ "$EUID" -eq 0 ]; then
    echo "Run the script as a user (not superuser)"
    exit 1
fi

# Variables
AGENT_NAME="open-drpc"
LAUNCHD_PLIST_PATH="$HOME/Library/LaunchAgents/$AGENT_NAME.plist"
SHARE_PATH="$HOME/.local/share/open-drpc"


# Delete LaunchAgent plist
launchctl stop "$AGENT_NAME"
launchctl unload "$LAUNCHD_PLIST_PATH"

rm -rf "$LAUNCHD_PLIST_PATH"

# Delete venv
rm -rf "$SHARE_PATH"
