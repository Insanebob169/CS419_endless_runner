#!/user/bin/python3
# host.py

import codecs, signal, sys, socket, select, termios, tty

serverFile = open("serverinfo.txt", "r")
server = serverFile.readline().strip()
port = serverFile.readline().strip()
port = int(port)
serverFile.close()

hostsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostsocket.connect((server, port))
# store this port to use to connect to the guest later
hostPort = hostsocket.getsockname()[1]
print("host port: " + str(hostPort))
hostName = socket.gethostname()
# this will be modified later to get the name from the user
testName = 'Jim'
hostIdentifier = '!host'
hostsocket.send(hostIdentifier.encode("ascii"))
serverMsg = hostsocket.recv(3).decode("utf-8").strip()
if serverMsg == '!':
	print("host: connected to server")
	hostsocket.send(testName.encode("ascii"))
	print("host: sent username, " + testName)

hostsocket.shutdown(socket.SHUT_RDWR)
hostsocket.close()

# start waiting for a guest to connect
hostsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# allow the socket to reuse the port without waiting for natural timeout
hostsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostsocket.bind((hostName, hostPort))
hostsocket.listen(1)
print(hostName + " listening on port " + str(hostPort))
(guestsocket, address) = hostsocket.accept()
hostsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("guest has connected")
# don't block while reading from guest loop
guestsocket.setblocking(False)
# main host/guest communication loop
oldSettings = termios.tcgetattr(sys.stdin)
try:
	tty.setcbreak(sys.stdin.fileno())
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
			guestCmd = guestsocket.recv(4096).decode("utf-8")
			print(guestCmd)
		except BlockingIOError:
			continue

			#print("stuck 5")
finally:
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldSettings)



