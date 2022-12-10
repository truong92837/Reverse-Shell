#!/usr/bin/env python3
import socket
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("192.168.1.13", 8080))
	s.listen(1)
	print ('Lang nghe tren cong 8080')
	conn, addr = s.accept()
	print ('Nhan duoc ket noi tu: ', addr)
	while True:
		command = input(">> ")
		if 'terminate' in command:
			conn.send('terminate')
			conn.close()
			break
		else:
			conn.send(command.encode())
			print(conn.recv(1024).decode("utf-8","ignore"))
def main ():
	connect()
main()
