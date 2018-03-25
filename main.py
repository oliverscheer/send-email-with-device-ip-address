#!/usr/bin/python3

import socket
import smtplib
import os

# Create a secrets.py file and place the following variables 
# sender_address = "<sender email address here>"
# sender_password = "<sender passwort here>"
# recipient_address = "<recipient address here>"

from secrets import sender_address
from secrets import sender_password
from secrets import recipient_address 


def get_device_ip_address():
    # On Windows
    # hostname = socket.gethostname()
    # result = "Hostname:  " + hostname
    # host = socket.gethostbyname(hostname)
    # result += "\nHost-IP-Address:" + host

    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ipaddr = s.getsockname()[0]
    gateway = gw[2]
    host = socket.gethostname()
    result = "IP:" + ipaddr + " Gateway:" + gateway + " Host: " + host
    return result

def send_email(text):
    try:
        message = "\"From: " + sender_address + "\nTo: " + recipient_address + "\nSubject: Device Information\n\n" + text + "\""

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_address, sender_password)
        server.sendmail(sender_address, recipient_address, message)
        server.close()
        print("Message sent:\n", message)

    except:
        print("failed to send email")

message = get_device_ip_address()
print("device data:")
print(message)
send_email(message)
print("Done.")

