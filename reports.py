#!/usr/bin/env python3

from datetime import datetime
import time
from datetime import date
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
import run





'''Returns processed.pdf'''
def generate_report(attachment, title, paragraph):
    stylesheet = getSampleStyleSheet()
    normalStyle = stylesheet['Normal']
    report = SimpleDocTemplate(title)
    report_title = Paragraph(title, stylesheet["h1"])
    report_info = Paragraph(paragraph, stylesheet["BodyText"])
    empty_line = Spacer(1,20)
    report.build([report_title, report_info ])
    return ''


