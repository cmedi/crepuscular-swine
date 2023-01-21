#!/usr/bin/env python3

import shutil
from socket import socket
import psutil
import emails


sender = 'automation@example.com'
receiver = 'username@example.com'



#check every 60 seconds

#Report an error if CPU usage is over 80%

if psutil.cpu_percent(1) > 80:
   emails.generate_email(sender, receiver, 'Error - CPU usage is over 80%', 'CPU usage is over 80%', attachment=None)
   

#Report an error if available disk space is lower than 20%
if psutil.disk_usage('/').percentage >= 80:
    emails.generate_email(sender, receiver, 'Error - Available disk space is less than 20%', 'Available disk space is lower than 20%', attachment=None)

#Report an error if available memory is less than 500MB
THRESHOLD = 500 * 1024 * 1024
if psutil.virtual_memory().available <= THRESHOLD:
    emails.generate_email(sender, receiver, 'Error - Available memory is less than 500MB', 'available memory is less than 500MB', attachment=None)


#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
def hostname_check():
  local_host_ip = socket.gethostbyname('localhost')
  return local_host_ip == "127.0.0.1"

if not hostname_check():
    emails.generate_email(sender, receiver, 'Error - localhost cannot be resolved to 127.0.0.1', 'hostname "localhost" cannot be resolved to "127.0.0.1"', attachment=None)