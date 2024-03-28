#!/bin/bash

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Extract the body of the response using curl with silent mode (-s) 
# and store it in a variable
response_body=$(curl -s "$1")

# Check for successful curl execution (exit code 0)
if [ $? -ne 0 ]; then
  echo "Error: curl failed to execute."
  exit 1
fi

# Get the size of the body (in bytes) using string length
body_size=${#response_body}

# Display the body size
echo "Body size: $body_size bytes"

