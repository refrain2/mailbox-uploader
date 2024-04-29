import os
import smtplib
import time
import random
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Log file directory
log_dir = r'D:\Mailbox uploader\log'

# Record information of successfully sent emails
def log_success(file_name, from_email, sending_time):
    today = datetime.date.today()
    log_file = os.path.join(log_dir, f'{today}.log')
    log_entry = f"{sending_time}: Email sent successfully {file_name}, from: {from_email}\n"
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_entry)

# Email configurations (Example)
email_credentials = [
    {"email": "example1@example.com", "password": "password1", "smtp_server": "smtp.example.com", "ports": [587, 25]},
    {"email": "example2@example.com", "password": "password2", "smtp_server": "smtp.example.com", "ports": [587, 25]},
    # Add more email accounts here
]

# Function to send email
def send_email(email_cred, to_email, file_path, file_name):
    try:
        if os.path.exists(file_path):
            msg = MIMEMultipart()
            msg['From'] = email_cred["email"]
            msg['To'] = to_email
            msg['Subject'] = file_name  # Change subject to file name

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(file_path, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {file_name}')
            msg.attach(part)

            for port in email_cred["ports"]:
                try:
                    server = smtplib.SMTP(email_cred["smtp_server"], port)
                    server.starttls() if port == 587 else None
                    server.login(email_cred["email"], email_cred["password"])
                    server.sendmail(email_cred["email"], to_email, msg.as_string())
                    server.quit()
                    print(f"Email sent successfully: {file_name}, using email: {email_cred['email']}")
                    log_success(file_name, email_cred["email"], datetime.datetime.now())  # Pass sender's email to log_success function
                    try:
                        os.remove(file_path)  # Delete file after sending
                        print(f"File deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting file: {e}")
                    return True
                except Exception as e:
                    print(f"Failed to send using {email_cred['email']}, port {port}: {e}")
                    continue
            print("All alternate ports failed to send.")
            return False
        else:
            print(f"File not found: {file_path}")
            return False
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Main function
def main():
    folder_path = r'D:\Save'  # Folder path
    send_interval = 15  # Send interval in seconds
    max_attempts = 10  # Maximum retry attempts

    print("Script execution started.")

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"Processing file: {file_path}")
            for attempt in range(max_attempts):
                print(f"Sending file: {file_path}")
                email_cred = random.choice(email_credentials)
                success = send_email(email_cred, "recipient@example.com", file_path, file_name)  # Use file name as subject
                if success:
                    break  # Break the retry loop if sent successfully
                else:
                    print(f"Sending failed. Retrying in {send_interval} seconds...")
                    time.sleep(send_interval)

    print("Script execution finished.")

if __name__ == "__main__":
    main()
