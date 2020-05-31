#!/usr/bin/env python3

import os
import shutil
import psutil
import socket

import emails

def check_cpu_usage():
    return psutil.cpu_percent(1) > 80

def check_disk_space():
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage("/")
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    if percent_free < 20:
        return True
    return False

def check_memory_usage():
    memory_use = psutil.virtual_memory()
    avl_memory = memory_use.available
    threshold = 500 * 1024 * 1024
    if avl_memory < threshold:
         return True
    return False

def check_resolve_hostname():
    ip_addr = socket.gethostbyname(socket.gethostname())
    return ip_addr != "127.0.0.1"

if __name__ == "__main__":
    checks=[
        (check_cpu_usage, "Error - CPU usage is over 80%"),
        (check_disk_space, "Error - Available disk space is less than 20%"),
        (check_memory_usage, "Error - Available memory is less than 500MB"),
        (check_resolve_hostname, "Error - localhost cannot be resolved to 127.0.0.1"),
    ]

    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."

    for check, subject in checks:
        if check():
            #print(subject)
            new_msg = emails.generate_email(sender, recipient, subject, body, "")
            emails.send_email(new_msg)
