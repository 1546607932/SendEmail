import smtplib
# Send PlainText
from email.mime.text import MIMEText
# Send Multiple Part
from email.mime.multipart import MIMEMultipart
# Send Email With Pictures
from email.mime.image import MIMEImage

# Part1:Basic Info
# host
mail_host = 'smtp.qq.com'
mail_user = '166268562'
mail_pass = 'mnnrmnfcrojocaaf'
sender = '166268562@qq.com'
receivers = ['1546607932@qq.com', '908805837@qq.com']

# Part2:Email Info
subject = 'Test Send To Multiple Users'
content = 'This is just a test to users!.\nIt seems OK!!!\n'

message = MIMEText(content, 'plain', 'utf-8')
message['From'] = sender
if len(receivers) > 1:
    message['To'] = receivers[0]
else:
    message['To'] = ','.join(receivers)
message['Subject'] = subject

# Part3:Login and Send Email
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('Error:', e)
