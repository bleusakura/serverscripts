from requests import get
from os import path
import smtplib, ssl
from datetime import datetime

ip = get('https://api.ipify.org').text

if not path.exists("current_ip.txt"):
	with open("current_ip.txt", "w+") as f:
		f.write(ip)
		quit()
else:
	with open("current_ip.txt", "r+") as f:
		current_ip = f.readline()
		current_ip.rstrip('\n')

if(current_ip != ip):
	with open("current_ip.txt", "w+") as f:
		f.write(ip)

	port = 465
	context = ssl.create_default_context()
	dateTimeObj = datetime.now()
	timestamp = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
	message = f"""\
	Subject: IP Change

	IP Changed from {current_ip} to {ip} at {timestamp}"""
	
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login("$senderemail", "$pythonscript$")
		server.sendmail("$senderemail", "$receiveremail", message)
