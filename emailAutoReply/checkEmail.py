import getpass, poplib
import email
import re
from emailReply import replyEmail, replySender
from emailData import USER, PASS


def emailTask():
    #login to the email on the gmail server
    mail = poplib.POP3_SSL('pop.gmail.com')#you may change this to be another email provider
    mail.user(USER)
    mail.pass_(PASS)
    #gets the total length of the inbox that have not already 
    #been visited by the bot
    numEmails = len(mail.list()[1])
    count = 0 

    if(numEmails>=1):
        replyEmail()
        for i in range(numEmails):
            for msg in mail.retr(i+1)[1]:
                #this will grab emails as they come in
                sender = re.findall(r'[\w\.-]+@[\w\.-]+',msg)
                for s in sender:
                    #make sure that the bot doesnt reply to itself or reply to gmail's auto messages
                    if s and count == 0 and s != 'put your email here so the bot wont reply to itself' and s != '@mx.google.com' and s!= '@mail.google.com':
                        count += 1 #makes sure you only reply once
                        replySender(sender)
                        print s #you can remove this but it is good for testing
    count = 0
    mail.quit()