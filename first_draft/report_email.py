#!/usr/bin/env python3

import os
from datetime import date
import reports
import run
import emails

if __name__ == "__main__":

    title ='processed.pdf'
    report_info = run.send_fruit()
    report_text = ''
    today = date.today()
    report_text += "Processed Update on {}<br/>".format(today)

    for fruit in report_info:
        report_text += "<br/><br/> name: {} <br/> weight: {} lbs <br/><br/>".format(fruit['name'],fruit['weight'])
    
    reports.generate_report(title, title, report_text)
    message= emails.generate_email('automation@example.com', 'username@example.com', 'Upload Completed - Online Fruit Store', 'All fruits are uploaded to our website successfully. A detailed list is attached to this email', 'processed.pdf')
    emails.send_email(message)