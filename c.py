import socket
def Main():
	host = "192.168.1.102"
	port = 1234
	
	s = socket.socket()
	s.connect((host,port))
	
	message = input("Enter your name : ")
	s.send(message.encode('utf-8'))

	stage = 0

	if(stage == 0):
		user_input = input("CHOOSE BAT or BOWL:")
		s.send(user_input.encode("utf-8"))
		data = s.recv(1024).decode('utf-8')
		print("Recieved from Server: "+data)
		stage = 1

	if(stage == 1):
		while message!='q':
			user_input = input("Enter 1/2/3/4/6:")
			s.send(user_input.encode("utf-8"))
			data = s.recv(1024).decode('utf-8')
			print("Recieved from Server Stage 1: "+data)
		
	s.close()
if __name__=='__main__':
	Main()