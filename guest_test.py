#!/user/bin/python3
# guest.py

import sys, socket, signal, select, termios, tty

serverFile = open("serverinfo.txt", "r")
server = serverFile.readline().strip()
port = serverFile.readline().strip()
port = int(port)
serverFile.close()

guestsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
guestsocket.connect((server, port))

#send guest identifier
guestIdentifier = "guest"
guestsocket.send(guestIdentifier.encode("ascii"))

#get the list of host names from the server
hostNames = guestsocket.recv(1024).decode("utf-8").strip()
print("guest: list of hostnames: " + hostNames)

hostChoice = input("Enter host name to join: ")

guestsocket.send(hostChoice.encode("ascii"))
rawHostAddress = guestsocket.recv(1024).decode("utf-8").strip()
print("guest: received host address " + rawHostAddress + " from server.")

guestsocket.close()
portFlag = True
hostAddress = ""
hostPort = ""
for x in rawHostAddress:
	if x in "() '\n\t":
		continue
	elif x == ',':
		portFlag = False
	else:
		if portFlag:
			hostAddress += x
		else:
			hostPort += x

guestsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
guestsocket.connect((hostAddress, int(hostPort)))

guestsocket.setblocking(False)

oldSettings  = termios.tcgetattr(sys.stdin)
try:
	tty.setcbreak(sys.stdin.fileno())

# main host/guest communication loop
	while True:
		if select.select([sys.stdin], [], [], 0) == ([sys.stdin],[],[]):
			#print("stuck 1")
			userCmd = sys.stdin.read(1)
			#print("stuck 2")
			if userCmd:
				#print("stuck 3")
				guestsocket.send(userCmd.encode("ascii"))
	
			#print("stuck 4")
		try:
			hostCmd = guestsocket.recv(4096).decode("utf-8")
			print(hostCmd)
		except BlockingIOError:
			continue
	
			#print("stuck 5")
finally:
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldSettings)
