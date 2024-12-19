# send_error_email.py
# This script gets the error message from weather.sh and sends a notification via email
# References:
    # https://medium.com/@thakuravnish2313/sending-emails-with-python-using-the-smtplib-library-e5db3a8ce69a
    # https://mailtrap.io/blog/python-send-html-email/ 
    # https://dabeaz-course.github.io/practical-python/Notes/03_Program_organization/05_Main_module.html
    # https://docs.python.org/3/library/__main__.html
    # https://realpython.com/if-name-main-python/

# Import required libraries
import os
import smtplib
from email.mime.text import MIMEText
import sys

# Fetch SMTP configuration from environment variables
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

def send_error_email(error_message):
    # Verify it the environment variables are present
    missing_vars = [var for var in ["SMTP_SERVER", "SMTP_PORT", "SENDER_EMAIL", "SENDER_PASSWORD", "RECIPIENT_EMAIL"] 
                    if os.getenv(var) is None]

    if missing_vars:
        print(f"Missing environment variables: {', '.join(missing_vars)}")
        sys.exit(1)

    # Create the email
    subject = "Weather Bash Script Error"
    body = (
        "GitHub Repository:\n"
        "https://github.com/tindraie/comp-infrastructure\n\n"
        f"The following error occurred in the weather.sh script:\n{error_message}"
    )
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Error notification email sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)

# To be ran only when the script is executed for testing purposes
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No error message provided.")
        sys.exit(1)

    # Get the error message and run the function
    error_message = sys.argv[1]
    send_error_email(error_message)
