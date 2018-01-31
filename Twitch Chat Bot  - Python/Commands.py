from Settings import OWNER, APIKey, summonerName, region
from Socket import sendMessage
from Bad_words import addBadWord, removeBadWord
from Riot_data import requestRankedData, requestSummonerData

commands = {'!opgg': 'http://eune.op.gg/summoner/userName=lee+sek', '!elo': 'Current elo:'}

def addCommand(s, message, commands):
	message_params = message.split(' ', 2)
	if len(message_params) != 3:
		print("addCommand::Error - Incorrect number of parameters")
	else:
		commands[message_params[1]] = message_params[2]
		sendMessage(s, "Command added:  " + message_params[1])

def removeCommand(s, message, commands):
	message_params = message.split(' ', 1)
	if len(message_params) != 2:
		print("removeCommand::Error - Incorrect number of parameters")
	else:
		del commands[message_params[1][0:len(message_params[1]) - 1]]
		sendMessage(s, "Command removed:  " + message_params[1])

def checkCommand(s, message, commands, user, bad_words):
	if user == OWNER and '!addcommand' in message:
		addCommand(s, message, commands)
		return
	if user == OWNER and '!removecommand' in message:
		removeCommand(s, message, commands)
		return
	if user == OWNER and '!addbadword' in message:
		addBadWord(s, message, bad_words)
		return
	if user == OWNER and '!removebadword' in message:
		removeBadWord(s, message, bad_words)
		return
		
	for key, item in commands.items():
		#To fix / think: len(message) is to big so i had to subtract one from it
		#if (len(message)-1 == len(key)) and (key in message):
		#Fix: add '\r' to key string
		if (len(message) == len(key + '\r')) and (key in message):
			if key == "!elo":
				requestSummonerData(region, summonerName, APIKey)
				
				responseJSON  = requestSummonerData(region, summonerName, APIKey)
				
				ID = responseJSON['id']
				ID = str(ID)
				
				responseJSON2 = requestRankedData(region, ID, APIKey)
				
				if not responseJSON2:
					sendMessage(s, item + " None")	
					return
				else:
					tier = responseJSON2[0]['tier']
					rank = responseJSON2[0]['rank']
					leaguePoints = responseJSON2[0]['leaguePoints']
					sendMessage(s, item + " " + str(tier) + " " + str(rank) + " " + str(leaguePoints) + " LP")
					return
			else:
				sendMessage(s, item)
				return
			 
	if len(commands) == 0 and user == OWNER and '!addcommand' in message:
		addCommand(s, message, commands)
