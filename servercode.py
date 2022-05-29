import socket
table={
        '192.168.20.1'.'5B.2E.12.1C',
        '192.168.8.15'.'AC.48.B2.50',
        '192.168.10.5'.'22.34.9A.FF',
        '192.168.26.3'.'D5.AB.6C.31',
        '192.168.2.11'.'E1.AA.73.88',
        '5B.2E.12.1C'.'192.168.20.1',
        'AC.48.B2.50'.'192.168.8.15',
        '22.34.9A.FF'.'192.168.10.5',
        'D5.AB.6C.31'.'192.168.26.3',
        'E1.AA.73.88'.'192.168.2.11',
      }

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((",5678))
s.listen()
clientsocket,address = s.accept()
print("Connection From", address, "Has Established")
ip = clientsocket.recv(1024)
ip = ip.decode("utf-8")
mac = table.get(ip, 'No entry for given address')
clientsocket.send(mac.encode())

