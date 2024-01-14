import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "chaitulucky007@gmail.com"
password = "lshk hykg jhim xtlg"

receiver = "chaitulucky003@gmail.com"

contex = ssl.create_default_context()

message = '''\
Subject: hi
how r u
hope u r fine
call me when u r free
i am learning python 
'''

with smtplib.SMTP_SSL(host,port,context=contex) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)



