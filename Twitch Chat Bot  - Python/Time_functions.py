from Socket import sendMessage
import time

def stopWatch(value):
	
	seconds = int(value)

	if seconds < 60:
		minutes = 0
		hours = 0
	elif seconds < 3600:
		minutes = seconds // 60
		seconds = seconds - 60*minutes
		hours = 0
	else:
		hours = seconds // 3600
		minutes = (seconds - 3600*hours) // 60
		seconds = seconds - 3600*hours - 60*minutes

	uptime = [hours, minutes, seconds]
	return uptime

	
def checkUptime(s, message, start):
	if (len(message) == len('!uptime' + '\r')) and ("!uptime" in message):
		end = time.time() 
		time_tab = stopWatch(end-start)
		uptime = str(time_tab[0]) + "h " + str(time_tab[1]) + "m " + str(time_tab[2]) + "s"
		sendMessage(s, uptime)
	
