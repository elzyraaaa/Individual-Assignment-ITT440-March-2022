import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost', 5678))
p = input("ARP or RARP:")
if(p == "ARP"):
	add = input ('Enter IP:')
elif(p == "RARP"):
	add = input ('Enter MAC:')
s.send(add.encode())
mac = s.recv(1024)
mac = mac.decode("utf-8")
if(p == "ARP"):
	print('MAC of ', add, 'is:', mac)
else: 
	 print('IP of ', add, 'is:', mac)

