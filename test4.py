import socket

hostname = input("Please enter website address:\n")

# IP lookup from hostname
print(f'The {hostname} IP Address is {socket.gethostbyname(hostname)}')