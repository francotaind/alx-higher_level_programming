#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl and retrieve body size
body_size=$(curl -sI "$1" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r\n')

# Display body size in bytes
echo "$body_size"

