from User import User, games, users

def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user

def getMessage(line):
	global message
	try:
		message = (line.split(":", 2))[2]
	except:
		message = ""
	return message

def Console(line):
	# gets if it is a user or twitch server
	if "PRIVMSG" in line:
		return False
	else:
		return True

def checkUser(s, message, PMSG, name, users, bad_words, games):
	for ppl in users:
		if ppl.name == name:
			tmp = False
			ppl.checkWarrnings(s, message, bad_words)
			ppl.checkParam(s, message)
			ppl.checkReward(s, message, PMSG, games)
			break
		elif ppl.name != name:
			tmp = True
		
	if tmp == True:
		user = User(name)
		users.append(user)
		user.checkWarrnings(s, message, bad_words)
		user.checkParam(s, message)
		user.checkReward(s, message, PMSG, games)
