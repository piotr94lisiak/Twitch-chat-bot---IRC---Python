from Socket import sendMessage

bad_words = {'warrning': ['fuck', 'fuuck', 'fuuuck'], 'timeout': ['niger']}

def timeOut(s, message, bad_words, user):
	for i in range(0, len(bad_words['timeout'])):
		if bad_words['timeout'][i] in  message:
			out = "/timeout " + user + " 1200"
			sendMessage(s, out)
			break

def addBadWord(s, message, bad_words):
	message_params = message.split(' ', 2)
	if len(message_params) != 3:
		print("addBadWord::Error - Incorrect number of parameters")
	else:
		if message_params[2] == 'warrning\r':
			bad_words['warrning'].append(message_params[1])
			sendMessage(s, "Word added to warrning list")
		elif message_params[2] == 'timeout\r':
			bad_words['timeout'].append(message_params[1])
			sendMessage(s, "Word added to timeout list")
		
def removeBadWord(s, message, bad_words):
	message_params = message.split(' ', 2)
	if len(message_params) != 3:
		print("removeBadWord::Error - Incorrect number of parameters")
	else:
		if message_params[2] == 'warrning\r':
			if message_params[1] in bad_words['warrning']:
				bad_words['warrning'].remove(message_params[1])
				sendMessage(s, "Word removed from warrning list")
		elif message_params[2] == 'timeout\r':
			if message_params[1] in bad_words['timeout']:
				bad_words['timeout'].remove(message_params[1])
				sendMessage(s, "Word removed from timeout list")
