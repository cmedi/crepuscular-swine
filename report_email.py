#!/usr/bin/env python3

import os
from datetime import date
import reports
import run
import emails

if __name__ == "__main__":
    path ="/tmp/processed.pdf"
    title ='processed.pdf'
    report_info = run.send_fruit()
    report_text = ''
    today = date.today()
    report_text += "Processed Update on {}<br/>".format(today)

    for fruit in report_info:
        report_text += "<br/><br/> name: {} <br/> weight: {} lbs <br/><br/>".format(fruit['name'],fruit['weight'])
    
    sender = 'automation@example.com' 
    receiver =  'student-02-474d0878134e'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    
    reports.generate_report(path, title, report_text)
    
