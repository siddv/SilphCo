import random

clearanceScale = {0: 'No Access', 1: 'Level 1 Clearance', 2: 'Level 2 Clearance',3: 'Level 3 Clearance', 4: 'Level 4 Clearance', 5: 'Top Level Clearance'}

class Silph:
	clearance = 0
	login1 = False 
	def list(self):
		print "\n/docs\n/survailence\n"	
	def login(self):
		print "Please enter your Silph unified access key"

silph = Silph()

print "Welcome to the Silph Co. mainframe"
while(True):
	userInput = raw_input(">")
	if userInput == "ssh silph.siddv.net":
		silph.login()
	elif userInput == "10237464":
		silph.login1 = True
	elif userInput == "ls":
		if silph.login1 != True:
			print "You need to log in to use this command"
		else:
			silph.ist()
	elif userInput == "quit":
		quit()