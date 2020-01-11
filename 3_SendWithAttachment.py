import smtplib
# Send PlainText
from email.mime.text import MIMEText
# Send Multiple Part
from email.mime.multipart import MIMEMultipart
# Send Email With Pictures
from email.mime.image import MIMEImage

# Part1:Basic Info
mail_host = 'smtp.qq.com'
mail_user = '166268562'
mail_pass = 'mnnrmnfcrojocaaf'
sender = '166268562@qq.com'
receivers = ['1546607932@qq.com']

# Part2:Email Info
subject = 'Welcome Sending Email By Code'
content = 'This is just a test.\nIt seems OK!!!\n'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receivers[0]
message['Subject'] = 'Welcome To Send Email By Code'

# Content in html file
with open('resource/extern.html', 'r') as f:
    content = f.read()
# Set html variables
part1 = MIMEText(content, 'html', 'utf-8')

# Add a txt File
with open('resource/externTest.txt','r') as h:
    content2 = h.read()
# Set txt Variables
part2 = MIMEText(content2, 'plain', 'utf-8')
part2['Content-Type'] = 'application/octet-stream'
part2['Content-Disposition'] = 'attachment;filename="TestTxt.txt"'

# Add a picture
with open('resource/My Favorite.gif', 'rb') as fp:
    picture = MIMEImage(fp.read())
    picture['Content-Type'] = 'application/octet-stream'
    picture['Content-Disposition'] = 'attachment;filename="TestPic.gif"'

message.attach(part1)
message.attach(part2)
message.attach(picture)

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
