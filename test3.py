import socket
hostname = socket.gethostname()
print(hostname)
ipaddress = socket.gethostbyname(hostname)
print(ipaddress)