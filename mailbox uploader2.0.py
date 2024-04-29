import os
import smtplib
import time
import random
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# 日志文件目录
log_dir = r'D:\Mailbox uploader\log'

# 记录成功发送的邮件信息
def log_success(file_name, from_email, sending_time):
    today = datetime.date.today()
    log_file = os.path.join(log_dir, f'{today}.log')
    log_entry = f"{sending_time}: 已发送邮件 {file_name}，发件邮箱: {from_email}\n"
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_entry)

# 邮件配置（范例）
email_credentials = [
    {"email": "example1@example.com", "password": "password1", "smtp_server": "smtp.example.com", "ports": [587, 25]},
    {"email": "example2@example.com", "password": "password2", "smtp_server": "smtp.example.com", "ports": [587, 25]},
    # Add more email accounts here
]

# 发送邮件函数
def send_email(email_cred, to_email, file_path, file_name):
    try:
        if os.path.exists(file_path):
            msg = MIMEMultipart()
            msg['From'] = email_cred["email"]
            msg['To'] = to_email
            msg['Subject'] = file_name  # 将主题改为文件名

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
                    print(f"邮件发送成功: {file_name}，使用邮箱: {email_cred['email']}")
                    log_success(file_name, email_cred["email"], datetime.datetime.now())  # 将发件邮箱传递给log_success函数
                    try:
                        os.remove(file_path)  # 发送后删除文件
                        print(f"文件已删除: {file_path}")
                    except Exception as e:
                        print(f"删除文件时出错: {e}")
                    return True
                except Exception as e:
                    print(f"使用邮箱 {email_cred['email']} 发送失败，端口号 {port}：{e}")
                    continue
            print("所有备选端口均发送失败。")
            return False
        else:
            print(f"未找到文件: {file_path}")
            return False
    except Exception as e:
        print(f"发送邮件时出错：{e}")
        return False

# 主函数
def main():
    folder_path = r'D:\Save'  # 文件夹路径
    send_interval = 15  # 发送间隔，单位为秒
    max_attempts = 10  # 最大重试次数

    print("脚本开始执行.")

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"处理文件: {file_path}")
            for attempt in range(max_attempts):
                print(f"发送文件: {file_path}")
                email_cred = random.choice(email_credentials)
                success = send_email(email_cred, "recipient@example.com", file_path, file_name)  # 将文件名作为主题
                if success:
                    break  # 如果成功发送，则跳出重试循环
                else:
                    print(f"发送失败. {send_interval} 秒后重试...")
                    time.sleep(send_interval)

    print("脚本执行结束.")

if __name__ == "__main__":
    main()
