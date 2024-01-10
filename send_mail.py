import smtplib, ssl
# smtp is for sending email
# ssl is for making secure connection b/w webserver and browser


def send_mail(receiver, message):
    host = "smtp.gmail.com"
    # specific for gmail and standard
    port = 465
    # its also standard
    username = "chaitulucky007@gmail.com"
    password = "lshk hykg jhim xtlg"

    context = ssl.create_default_context()
    # for creation of secure context for sending emial securely we need ssl lib

    # smtplib.SMTP_SSL is used to establish a connection to the SMTP server with SSL.
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


