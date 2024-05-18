# Mailbox Uploader Script

This script automates the process of sending files from a specified folder as email attachments using a list of predefined email accounts. It logs the details of successfully sent emails and deletes the sent files after successful transmission.

## Features
- Sends files as email attachments.
- Supports multiple email accounts and ports.
- Logs details of successfully sent emails.
- Deletes files after successful email transmission.
- Retries sending on failure with a configurable interval and maximum attempts.

## Requirements
- Python 3.x
- Required libraries: `smtplib`, `email`, `os`, `time`, `random`, `datetime`

## Setup
1. Clone this repository to your local machine.
2. Install the required Python libraries if they are not already installed.
3. Edit the script to configure the email credentials and other settings.

### Email Credentials Configuration
In the script, update the `email_credentials` list with your email accounts' details:
```python
email_credentials = [
    {"email": "example1@example.com", "password": "password1", "smtp_server": "smtp.example.com", "ports": [587, 25]},
    {"email": "example2@example.com", "password": "password2", "smtp_server": "smtp.example.com", "ports": [587, 25]},
    # Add more email accounts here
]
```

### Folder Path Configuration
Set the folder path where the files to be sent are stored:
```python
folder_path = r'D:\Save'  # Replace with your folder path
```

### Log Directory Configuration
Set the log directory path where the logs will be stored:
```python
log_dir = r'D:\Mailbox uploader\log'  # Replace with your log directory path
```

### Send Interval and Max Attempts Configuration
Configure the send interval (in seconds) and maximum attempts:
```python
send_interval = 15  # Send interval in seconds
max_attempts = 10  # Maximum retry attempts
```

## Usage
Run the script using Python:
```bash
python mailbox_uploader.py
```

The script will iterate over the files in the specified folder, attempt to send them via email, and log the results. It will delete the files after they are successfully sent.

## Logging
The script logs the details of successfully sent emails in daily log files located in the specified log directory. Each log entry includes the timestamp, the file name, and the sender's email.

## Error Handling
If sending fails, the script retries based on the configured interval and maximum attempts. It logs any errors encountered during the process.

## Example Log Entry
```
2024-05-18 14:35:27: 已发送邮件 example.txt，发件邮箱: example1@example.com
```

---

# 邮箱上传脚本

此脚本通过使用预定义的邮箱列表，自动将指定文件夹中的文件作为邮件附件发送。它记录成功发送的邮件信息并在成功发送后删除发送的文件。

## 功能
- 将文件作为邮件附件发送。
- 支持多个邮箱和端口。
- 记录成功发送的邮件信息。
- 成功发送邮件后删除文件。
- 发送失败时可重试，重试间隔和最大重试次数可配置。

## 需求
- Python 3.x
- 所需库：`smtplib`，`email`，`os`，`time`，`random`，`datetime`

## 设置
1. 将此存储库克隆到本地机器。
2. 安装所需的Python库（如果尚未安装）。
3. 编辑脚本以配置邮箱凭据和其他设置。

### 邮箱凭据配置
在脚本中，更新`email_credentials`列表以包含您的邮箱账户的详细信息：
```python
email_credentials = [
    {"email": "example1@example.com", "password": "password1", "smtp_server": "smtp.example.com", "ports": [587, 25]},
    {"email": "example2@example.com", "password": "password2", "smtp_server": "smtp.example.com", "ports": [587, 25]},
    # Add more email accounts here
]
```

### 文件夹路径配置
设置存储待发送文件的文件夹路径：
```python
folder_path = r'D:\Save'  # 替换为您的文件夹路径
```

### 日志目录配置
设置存储日志的目录路径：
```python
log_dir = r'D:\Mailbox uploader\log'  # 替换为您的日志目录路径
```

### 发送间隔和最大尝试次数配置
配置发送间隔（以秒为单位）和最大尝试次数：
```python
send_interval = 15  # 发送间隔（秒）
max_attempts = 10  # 最大重试次数
```

## 使用方法
使用Python运行脚本：
```bash
python mailbox_uploader.py
```

脚本将遍历指定文件夹中的文件，尝试通过邮件发送，并记录结果。文件成功发送后将被删除。

## 日志
脚本在指定的日志目录中以每天的日志文件记录成功发送的邮件信息。每条日志记录包括时间戳、文件名和发件人的邮箱。

## 错误处理
如果发送失败，脚本将根据配置的间隔和最大尝试次数进行重试。它会记录发送过程中遇到的任何错误。

## 日志示例
```
2024-05-18 14:35:27: 已发送邮件 example.txt，发件邮箱: example1@example.com
```

Feel free to contribute or raise issues on GitHub. Happy mailing!
