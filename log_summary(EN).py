import os
import pandas as pd
import datetime
import re

# Directory containing log files
log_dir = r'D:\Mailbox uploader\log'

# Output Excel filename with current date
output_excel_filename = 'log_summary_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.xlsx'
output_excel_path = os.path.join(log_dir, output_excel_filename)

# Create an empty DataFrame to store all log data
all_logs_df = pd.DataFrame(columns=['Email ID', 'File Name', 'Sender Email', 'Sending Time'])

# Regular expression pattern for parsing log files
log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+): Sent email (.+?) from email: (.+)')

# Iterate through all files in the log directory
for root, dirs, files in os.walk(log_dir):
    for file_name in files:
        # Check if the file is a .log file
        if file_name.endswith('.log'):
            file_path = os.path.join(root, file_name)
            print(f"Processing log file: {file_path}")  # Debugging information
            # Read the .log file
            with open(file_path, 'r', encoding='utf-8') as log_file:
                lines = log_file.readlines()
                for line in lines:
                    # Parse each line of the log using regular expressions
                    match = log_pattern.match(line.strip())
                    if match:
                        sending_time_str, log_file_name, from_email = match.groups()
                        # Generate email ID
                        sending_time_dt = datetime.datetime.strptime(sending_time_str.split('.')[0], "%Y-%m-%d %H:%M:%S")
                        email_id = sending_time_dt.strftime("%Y%m%d%H%M%S")
                        # Add the record to the DataFrame
                        all_logs_df = pd.concat([all_logs_df, pd.DataFrame([[email_id, log_file_name, from_email, sending_time_str]], columns=all_logs_df.columns)], ignore_index=True)
                    else:
                        print(f"Unparseable log line: {line.strip()}")  # Debugging information

# Write the merged DataFrame to a new Excel file
if not all_logs_df.empty:
    all_logs_df.to_excel(output_excel_path, index=False)
    print(f"All log files have been merged into {output_excel_path}")
else:
    print("No log data parsed.")
