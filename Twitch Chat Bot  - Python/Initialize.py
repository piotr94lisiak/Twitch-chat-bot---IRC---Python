import string
import socket
from Socket import sendMessage

def joinRoom(s):
	
	readbuffer = "".encode()
	Loading = True
	
	while Loading:
		readbuffer = s.recv(1024)
		readbuffer = readbuffer.decode()
		temp = readbuffer.split("\n")
		readbuffer = readbuffer.encode()
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	sendMessage(s, "Successfully joined Chat")


def loadingComplete(line):
	
	if ("End of /NAMES list" in line):
		return False
	else:
		return True
