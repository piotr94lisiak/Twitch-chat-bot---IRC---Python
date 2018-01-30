import socket
from Settings import HOST, PORT, PASS, NICK, CHANNEL

def openSocket():
	
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send(("PASS " + PASS + "\r\n").encode())
	s.send(("NICK " + NICK + "\r\n").encode())
	s.send(("JOIN #" + CHANNEL + "\r\n").encode())
	
	return s


def sendMessage(s, message):
	
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send((messageTemp + "\r\n").encode())
	print("Send: " + messageTemp)

#s.send(("CAP REQ :twitch.tv/tags\r\n").encode())
