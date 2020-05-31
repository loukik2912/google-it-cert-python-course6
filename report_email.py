#!/usr/bin/env python3

import os
import glob
import datetime
from datetime import date
import reports
import emails

def get_title():
 today = date.today()
 d2 = "Processed Update of " + today.strftime("%B %d, %Y")
 print(d2)
 return d2

def generate_data():
 contents_list = list()

 for fileName in glob.glob('supplier-data/descriptions/*.txt'):
  with open(fileName, 'r') as f:
   content = f.read().splitlines()
   one_elt = 'name: ' + content[0] + '<br/>weight: ' + content[1]
   #print(one_elt)
   contents_list.append(one_elt)

 print(contents_list)
 return contents_list


if __name__ == "__main__":
  reports.generate_report(attachment="/tmp/processed.pdf", title=get_title(), paragraph=generate_data())

  receiver = "{}@example.com".format(os.environ.get('USER'))

  for filename in glob.glob("/home/student-02-575f8e6a78b4/*.py"):
   my_message = emails.generate_email(sender="automation@example.com", recipient=receiver, subject=filename,
                body="a PY script", attachment_path=filename)
   emails.send_email(my_message)
