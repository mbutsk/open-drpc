#!/bin/bash

# Superuser check
if [ "$EUID" -eq 0 ]; then
    echo "Run the script as a user (not superuser)"
    exit 1
fi

# Systemctl check
if ! command -v systemctl >/dev/null 2>&1; then
    echo "Install systemd using your distribution's package manager."
    exit 1
fi

# Variables
SERVICE_NAME="open-drpc"
SHARE_PATH="/usr/share/open-drpc"
SYSTEMD_SERVICE_PATH="$HOME/.config/systemd/user/$SERVICE_NAME.service"

# Delete venv
sudo rm -rf "$SHARE_PATH"

# Delete service
rm -rf "$SYSTEMD_SERVICE_PATH"

systemctl --user stop "$SERVICE_NAME"
systemctl --user disable "$SERVICE_NAME"
systemctl --user daemon-reload