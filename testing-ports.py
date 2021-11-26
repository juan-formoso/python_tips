import socket

# ports to be tested
ports = [21, 22, 80, 8080, 443, 53, 3306, 3389]

# assign ip
ip = 'XXX.XXX.XXX.XXX'

for port in ports:
	# create socket
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.1)
	# connection test
	try:
		response = client.connect_ex((ip, port))
		if response == 0:
			print('sucess - connection established port: ', port)
		else:
			print('error - connection failed port: ', port)
	except:
		exit(1)