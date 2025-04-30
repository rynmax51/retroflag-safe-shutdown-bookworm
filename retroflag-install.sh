#!/bin/bash

# Exit if any command fails
set -e

# Define paths
INSTALL_DIR="/opt/RetroFlag"
SCRIPT_PATH="$INSTALL_DIR/SafeShutdown.py"
SERVICE_PATH="/etc/systemd/system/safeshutdown.service"

echo "Starting RetroFlag Safe Shutdown installer..."

# Make sure we're running as root
if [[ $EUID -ne 0 ]]; then
    echo "Please run this installer as root (use sudo)."
    exit 1
fi

# Create install directory if missing
if [ ! -d "$INSTALL_DIR" ]; then
    echo "Creating directory: $INSTALL_DIR"
    mkdir -p "$INSTALL_DIR"
fi

# Copy SafeShutdown.py
echo "Copying SafeShutdown.py..."
cp ./SafeShutdown.py "$SCRIPT_PATH"

# Create systemd service file
echo "Creating systemd service..."
cat <<EOF > "$SERVICE_PATH"
[Unit]
Description=Safe Shutdown Service for Retroflag Case
After=network.target

[Service]
ExecStart=/usr/bin/python3 $SCRIPT_PATH
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

# Set permissions
chmod 644 "$SERVICE_PATH"
chmod +x "$SCRIPT_PATH"

# Reload systemd
echo "Reloading systemd..."
systemctl daemon-reload

# Enable service
echo "Enabling safeshutdown service..."
systemctl enable safeshutdown

# Start service
echo "Starting safeshutdown service..."
systemctl start safeshutdown

echo "Installation complete! Safe Shutdown service is running."
