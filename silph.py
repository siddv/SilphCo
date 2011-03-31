import random

clearanceScale = {0: 'No Access', 1: 'Level 1 Clearance', 2: 'Level 2 Clearance',3: 'Level 3 Clearance', 4: 'Level 4 Clearance', 5: 'Top Level Clearance'}

class Silph:

	clearance = 0
	login1 = False 
	def list(self):
		print "You've requested idents for silphco.com"
		print "USERNAME: Silphadmin"	
		print "PASSWORD: SWJ698"
		
	def login(self):
		print "Please enter your Silph unified access key"
silph = Silph()

print "Welcome to the Silph Co. mainframe. Type 'help' for a list of commands"
while(True):
	userInput = raw_input(">")
	if userInput == "ssh silphco.com":
		silph.login()
	elif userInput == "LJ43":
		silph.login1 = True
		print "Connection successful"
	elif userInput == "getpass":
		if silph.login1 != True:
			print "You need to ssh into the server to use this command"
		else:
			silph.list()
	elif userInput == "help":
		print "ssh <server>"
		print "getpass"
		print "quit"
	elif userInput == "quit":
		quit()