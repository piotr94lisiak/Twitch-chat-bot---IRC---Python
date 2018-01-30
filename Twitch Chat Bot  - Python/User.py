from Settings import OWNER
from Socket import sendMessage
import random
from Bad_words import bad_words

games = {'waiting': [['name1', 'code1'],['name2', 'code2']], 'sended': []}

class User:
	
	def __init__(self, name):
		self.name = name
		self.message = ""
		self.points = 0
		self.warrnings = 0
		self.bans = 0
	
	def addWarrning(self, warrnings):
		self.warrnings += warrnings
	
	def addBan(self, bans):
		self.bans += bans
		
	def addPoint(self, points):
		self.points += points
		
	def zeroWarrnings(self):
		self.warrnings = 0
		
	def zeroBans(self):
		self.bans = 0
		
	def checkWarrnings(self, s, message, bad_words):
		for i in range(0, len(bad_words['warrning'])):
			if bad_words['warrning'][i] in  message and self.name != OWNER:
				self.addWarrning(1)
				if self.warrnings < 3:
					sendMessage(s, self.name + " - Warrning nr." + str(self.warrnings))
					break
				elif self.warrnings >= 3:
					self.checkBans(s, message)
				else:
					print("checkWarrnings::Error - Something wrong with self.warrning")
		
	def checkBans(self, s, message):
		if self.warrnings >= 3:
			self.addBan(1)
			if self.bans == 1:
				out = "/timeout " + self.name + " 60"
				sendMessage(s, out)
			elif self.bans == 2:
				out = "/timeout " + self.name + " 600"
				sendMessage(s, out)
			elif self.bans == 3:
				out = "/timeout " + self.name + " 3600"
				sendMessage(s, out)
				self.zeroWarrnings()
				self.zeroBans()
			else:
				print("checkBans::Error - Something wrong with self.bans")
	
	def checkParam(self, s, message):
		if (len(message) == len("!bans" + '\r')) and ("!bans" in message):
			sendMessage(s, self.name + " - Amount of bans: " + str(self.bans))
			return True
		if (len(message) == len("!warrnings" + '\r')) and ("!warrnings" in message):
			sendMessage(s, self.name + " - Amount of warrnings: " + str(self.warrnings))
			return True
		if (len(message) == len("!points" + '\r')) and ("!points" in message):
			sendMessage(s, self.name + " - Amount of points: " + str(self.points))
			return True
			
	def checkReward(self, s, message, PMSG, games):
		if (len(message) == len("!game" + '\r')) and ("!game" in message):
			if len(games['waiting']) == 0:
				sendMessage(s, "Database of games is empty at the moment")
			elif self.points < 10000:
				sendMessage(s, "Not enought points")
			elif self.points >= 10000:
				tmp = games['waiting'].pop(random.randint(0, len(games['waiting']) - 1))
				sendMessage(s, PMSG + "Gra: " + tmp[0] + " Kod: " + tmp[1])
				games['sended'].append(tmp)
				self.points = self.points - 10000
			
	
users = [User(OWNER)]
