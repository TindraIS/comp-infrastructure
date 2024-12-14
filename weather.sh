# Shebang line that specifies the path to the interpreter that should be used to execute the script
#!/bin/bash

# Set the output directory
output_dir="data/weather"

# Create the directory if it doesn't exist
mkdir -p "$output_dir"

# Create variables for the filename, path, and weather data URL 
filename="$(date +%Y%m%d_%H%M%S).json"
output_file="$output_dir/$filename"
weather_url="https://prodapi.metweb.ie/observations/athenry/today"

# Download the weather data and save it with the timestamped filename
wget -O "$output_file" "$weather_url"

# Data validation
if jq . "$output_file" > /dev/null 2>&1; then
    echo "$filename is valid."
else
    echo "$filename is invalid."
    # Remove the invalid file and display message
    rm -f "$output_file"
    echo "Invalid file removed."
fi
