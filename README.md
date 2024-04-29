# mailbox-uploader
This script serves as an automated email sender capable of handling attachments, leveraging multiple email accounts for delivery reliability. It aims to streamline the process of sending emails with attachments by systematically scanning a designated folder for files, attaching them to outgoing emails, and dispatching them to specified recipients. In cases where delivery encounters obstacles, such as connectivity issues or server limitations, the script dynamically switches between different email accounts and communication ports to maximize the chances of successful transmission.

Key Features:

Automated Attachment Handling: The script automatically locates files within a specified directory and attaches them to outgoing emails.
Email Account Rotation: It utilizes multiple email accounts to send emails, increasing the chances of successful delivery and minimizing the impact of potential email server restrictions or limitations.
Dynamic Port Selection: To overcome potential port blocking or network issues, the script intelligently selects between available communication ports (e.g., 587 or 25) during the transmission process.
Logging and Maintenance: Successful email deliveries are logged, providing a record of sent emails for reference. Furthermore, sent files are promptly deleted after successful transmission, ensuring efficient resource management and maintaining folder organization.

这个脚本是一个自动化的邮件发送工具，可以处理附件，并利用多个电子邮件账户提高邮件发送的可靠性。它旨在通过系统地扫描指定文件夹中的文件，将其作为附件添加到发件邮件中，并将其发送给指定的收件人，来简化发送带附件的邮件的过程。在遇到发送障碍的情况下，比如连接问题或服务器限制，脚本会动态地在不同的电子邮件账户和通信端口之间切换，以最大程度地提高传输成功的机会。

关键特性：

自动化附件处理： 脚本会自动定位指定目录中的文件，并将它们作为附件添加到发件邮件中。
电子邮件账户轮换： 使用多个电子邮件账户发送邮件，增加发送成功的可能性，并最大程度地减少电子邮件服务器限制或限制的影响。
动态端口选择： 为了克服可能的端口屏蔽或网络问题，脚本在传输过程中智能地选择可用的通信端口（例如587或25）。
日志记录和维护： 记录成功发送的邮件，提供已发送邮件的记录供参考。此外，成功传输后，已发送的文件会立即被删除，以确保资源的有效管理和文件夹的组织。
