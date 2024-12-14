# send_error_email.py
# This script gets the error message from weather.sh and sends a notification via email
# References:
    # https://medium.com/@thakuravnish2313/sending-emails-with-python-using-the-smtplib-library-e5db3a8ce69a
    # https://mailtrap.io/blog/python-send-html-email/ 

# Import required libraries
import os
import smtplib
from email.mime.text import MIMEText
import sys
from dotenv import load_dotenv  

# Load variables from .env file
load_dotenv()

# Configure SMTP to fetch credentials from environment variables
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

# Get the error message from the Bash script
if len(sys.argv) < 2:
    print("No error message provided.")
    sys.exit(1)

error_message = sys.argv[1]

# Create the email
subject = "Weather Bash Script Error"
body = f"GitHub Repository: \nhttps://github.com/TindraIS/comp-infrastructure \n\nThe following error occurred in the weather.sh script:\n{error_message}"
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_email

try:
    # Connect to the server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Error notification email sent.")
except Exception as e:
    print(f"Failed to send email: {e}")
    sys.exit(1)
