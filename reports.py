#!/usr/bin/env python3

import os
import glob
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report(attachment, title, paragraph):
 styles = getSampleStyleSheet()

 report = SimpleDocTemplate(attachment)

 report_title = Paragraph(title, styles["h1"])
 #report_info = Paragraph(paragraph, styles["BodyText"])
 empty_line = Spacer(1,20)

 content_list = [report_title]
 for each_line in paragraph:
  content_list.append(empty_line)
  content_list.append(Paragraph(each_line, styles["BodyText"]))
 
 report.build(content_list)
