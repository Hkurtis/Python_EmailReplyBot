import smtplib
from emailData import USER, PASS

#this function will email you when your bot has replied to an email
def replyEmail():
    content = ''#put whatever message you want to send here

    #send message through gmail port 587 
    mail = smtplib.SMTP('smtp.gmail.com',587)

    #tells the server who you are
    mail.ehlo()

    mail.starttls()

    mail.login(USER,PASS)
    #first parameter is the email sending the message
    #second parameter is the receiver of the message
    mail.sendmail(USER,'',content)

    mail.close()

#this function will automatically send out a reply to whoever sent you an email
def replySender(sender):

    #send message through gmail port 587 
    mail = smtplib.SMTP('smtp.gmail.com',587)

    #tells the server who you are
    mail.ehlo()

    mail.starttls()

    mail.login(USER,PASS)
    #first parameter is the email sending the message
    #second parameter is the receiver
    #third is the content you want to send
    replyE = ''#Email you want to send out
    mail.sendmail(USER,sender,replyE)

    mail.close()