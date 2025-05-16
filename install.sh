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
SCRIPT_PATH="$(pwd)"
SYSTEMD_SERVICE_PATH="$HOME/.config/systemd/user/$SERVICE_NAME.service"
SHARE_PATH="/usr/share/open-drpc"

# Venv
sudo python3 -m venv "$SHARE_PATH/venv"
sudo "$SHARE_PATH/venv/bin/pip" install -r "$SCRIPT_PATH/requirements.txt"

# Service creating
mkdir -p "$(dirname "$SYSTEMD_SERVICE_PATH")"

cat <<EOF > "$SYSTEMD_SERVICE_PATH"
[Unit]
Description=Steam Discord RPC
After=network.target

[Service]
ExecStart=$SHARE_PATH/venv/bin/python $SCRIPT_PATH/open-drpc/main.py
Restart=always

[Install]
WantedBy=default.target
EOF

# Systemctl reboot and start service
systemctl --user daemon-reload
systemctl --user enable "$SERVICE_NAME"
systemctl --user start "$SERVICE_NAME"