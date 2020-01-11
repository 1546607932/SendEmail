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
# username
mail_user = '166268562'
# password  Attention:Password of qq is smtpcode
mail_pass = 'mnnrmnfcrojocaaf'
# sender
sender = '166268562@qq.com'
# receivers
receivers = ['1546607932@qq.com']

# Part2:Email Info
# SubjectInfo
subject = 'Welcome Sending Email By Code'
# Content
content = 'This is just a test.\nIt seems OK!!!\n'

# MIME:Multipurpose Internet Mail Extension
message = MIMEText(content, 'plain', 'utf-8')
# Sender Info
message['From'] = sender
# Receiver Info
message['To'] = receivers[0]
# Subject
message['Subject'] = subject

# Part3:Login and Send Email
try:
    # Define smtp Object
    smtpObj = smtplib.SMTP()
    # Connect To Server
    smtpObj.connect(mail_host, 25)
    # Login To Server
    smtpObj.login(mail_user, mail_pass)
    # Send Email
    smtpObj.sendmail(sender, receivers, message.as_string())
    # Exit
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('Error:', e)
