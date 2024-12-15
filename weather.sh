# Shebang line that specifies the path to the interpreter that should be used to execute the script
#!/bin/bash

# Create variables for the output directory, log file, filename, path, and weather data URL
output_dir="data/weather"
log_file="weather.log" 
filename="$(date +%Y%m%d_%H%M%S).json"
output_file="$output_dir/$filename"
weather_url="https://prodapi.metweb.ie/observations/athenry/today"

# Function to send error notifications
send_error_email() {
    error_message="$1"
    python3 send_error_email.py "$error_message"
}

# Log the start of the download
echo -e "\n--------------------------------------------------------------" >> "$log_file"
echo "$(date) [INFO]: Fetching weather data from Met Eireann API endpoint" >> "$log_file"

# Fetch the weather data and save it with the timestamped filename
if wget -O "$output_file" "$weather_url" >> "$log_file" 2>&1; then
    echo "$(date) [INFO]: Successfully downloaded $filename" >> "$log_file"
else
    error_message="$(date) [ERROR]: Failed to download weather data from $weather_url. Check the URL or network connection."
    echo "$error_message" >> "$log_file"
    send_error_email "$error_message"
    exit 1
fi

# Validate the JSON data and remove the newly created file if data isn't valid
if jq . "$output_file" > /dev/null 2>&1; then
    echo "$(date) [INFO]: $filename is valid." >> "$log_file"
    echo "$filename is valid."
else
    error_message="$(date) [ERROR]: $filename is invalid. Removing file."
    echo "$error_message" >> "$log_file"
    rm -f "$output_file"
    send_error_email "$error_message"
    echo "$filename is invalid."
    exit 1
fi
