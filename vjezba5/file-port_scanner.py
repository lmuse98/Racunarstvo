import datetime
import socket
import time
#from local_machine_info import print_machine_info

start_time = time.time()

print ("Vrijeme pokretanja programa: ")
print (datetime.datetime.now())
print ("Program se izvodi: ")
#print_machine_info()

print ("--------------------------------------------------")
print ("Unesite adresu hosta koju testirate: ")
target = input(">>")
targetIP = socket.gethostbyname(target)

print ("Skeniram host: %s, IP adresu: %s" % (target, targetIP))
print ("Unesite port od kojeg zelite skeniranje?")
start = int(input("Pocetni port >>"))
end = int(input("Zavrsni port >>"))

for Port in range(int(start),int(end)+1):
	sock = socket.socket()
	result = sock.connect_ex((targetIP,Port))
	if result == 0:
		print("Port %s " %(Port))
	else:
		print ("Port je zatvoren %s" %(Port))
	sock.close()

elapsed_time = time.time() - start_time

print ("Skeniranje portova završeno!!!")
print ("Trajanje: %s " %elapsed_time)