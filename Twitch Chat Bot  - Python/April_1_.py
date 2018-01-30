from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import OWNER
import time
from User import users, games
from Time_functions import stopWatch, checkUptime
from Info_functions import getMessage, getUser, Console, checkUser
from Bad_words import timeOut, bad_words
from Commands import checkCommand, commands

s = openSocket()
joinRoom(s)
start = time.time() 
readbuffer = ""

while True:
	
	try:
		readbuffer = s.recv(1024)
		readbuffer = readbuffer.decode()
		temp = readbuffer.split("\n")
		readbuffer = readbuffer.encode()
		readbuffer = temp.pop()
	except:
		temp = ""
	for line in temp:
		if line == "":
			break
		# So twitch doesn't timeout the bot.
		if "PING" in line and Console(line):
			msg = "PONG tmi.twitch.tv\r\n".encode()
			s.send(msg)
			print(msg)
		# get user
		name = getUser(line)
		# get message send by user
		message = getMessage(line)
			
		# for owner to see the chat from CMD
		print(name + ": " + message)
		# sends private msg to the user (start line)
		PMSG = "/w " + name + " "
		
	checkUser(s, message, PMSG, name, users, bad_words, games)
	timeOut(s, message, bad_words, name)
	checkCommand(s, message, commands, name, bad_words)
	checkUptime(s, message, start)
		

