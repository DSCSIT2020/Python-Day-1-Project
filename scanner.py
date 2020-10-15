#!/bin/python3	
import sys
import socket
from datetime import datetime as dt
#Define _ targate
if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print ("Invalid Ammount of arguments: ")
	print ("Syntax: python3 scanner.py <ip>")
#Add a preety banner

print ("-"*50)
print ("Scanning Target " +target)
print ("Time Started: " +str(dt.now()))
print ("-"*50)

try: 
	for port in range (1,65535):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.0000000000000001)
		result = s.connect_ex((target,port))
		#print ("cheaking port {}" .format(port))
		if result ==0:
			print ("port {} is open".format(port))
		s.close()
except keyboardInterrupt:
	print ("\n Exiting Program")
	sys.exit()
except socket.error:
	print ("Couldn't connect to the server.")
	sys.exit()