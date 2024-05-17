import os
import pandas as pd
import datetime
import re

# 日志文件目录
log_dir = r'D:\Mailbox uploader\log'
output_excel_filename = 'log_summary_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.xlsx'
output_excel_path = os.path.join(log_dir, output_excel_filename)

# 创建一个空的 DataFrame 来存储所有的日志数据
all_logs_df = pd.DataFrame(columns=['邮件ID', '文件名', '发件邮箱', '发送时间'])

# 正则表达式模式，用于解析日志文件
log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+): 已发送邮件 (.+?)，发件邮箱: (.+)')

# 遍历日志文件目录下的所有文件
for root, dirs, files in os.walk(log_dir):
    for file_name in files:
        # 检查文件是否为 .log 文件
        if file_name.endswith('.log'):
            file_path = os.path.join(root, file_name)
            print(f"处理日志文件: {file_path}")  # 调试信息
            # 读取 .log 文件
            with open(file_path, 'r', encoding='utf-8') as log_file:
                lines = log_file.readlines()
                for line in lines:
                    # 使用正则表达式解析每行日志
                    match = log_pattern.match(line.strip())
                    if match:
                        sending_time_str, log_file_name, from_email = match.groups()
                        # 生成邮件ID
                        sending_time_dt = datetime.datetime.strptime(sending_time_str.split('.')[0], "%Y-%m-%d %H:%M:%S")
                        email_id = sending_time_dt.strftime("%Y%m%d%H%M%S")
                        # 将记录添加到 DataFrame
                        all_logs_df = pd.concat([all_logs_df, pd.DataFrame([[email_id, log_file_name, from_email, sending_time_str]], columns=all_logs_df.columns)], ignore_index=True)
                    else:
                        print(f"无法解析的日志行: {line.strip()}")  # 调试信息

# 将合并后的 DataFrame 写入一个新的 Excel 文件
if not all_logs_df.empty:
    all_logs_df.to_excel(output_excel_path, index=False)
    print(f"所有日志文件已合并到 {output_excel_path}")
else:
    print("没有解析到任何日志数据。")
