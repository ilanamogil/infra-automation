#!/bin/bash

# Script to install nginx if it doesn't exist

# Check if nginx is already installed
if command -v nginx &> /dev/null; then
    echo "nginx is already installed"
    echo "Version: $(nginx -v 2>&1)"
    exit 0
fi

echo "nginx not found. Installing nginx..."

echo "Installing nginx for Ubuntu..."
sudo apt-get update
sudo apt-get install -y nginx

# Verify installation
if command -v nginx &> /dev/null; then
    echo "nginx successfully installed"
    echo "Version: $(nginx -v 2>&1)"
    exit 0
else
    echo "Failed to install nginx"
    exit 1
fi
