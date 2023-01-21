#!usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(from_, to, subject, body, attachment=None):
    '''Creates an email with an attachment.'''
    #Basic email formatting
    message = email.message.EmailMessage()
    message["From"] = from_
    message["To"] = to
    message["Subject"] = subject

    message.set_content(body)
    #Process the attachment and add it to the email
    
    if attachment !=  None:
        attachment_filename = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment, 'rb') as ap:
            message.add_attachment(ap.read(),
            maintype = mime_type, 
            subtype=mime_subtype, 
            filename=attachment_filename)
    return message

def send_email( message_to_send ):
    
    mail_server = smtplib.SMTP('localhost')
    mail_server.send(message)
    mail_server.quit()

