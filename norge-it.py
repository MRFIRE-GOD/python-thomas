print("---------------------------------------------")
#Din pc informasjon
import platform
my_system = platform.uname()

print(f"Hviken type system : {my_system.system}")
print(f"Navnet på enhten : {my_system.node}")
print(f"hvilken type pc-en er : {my_system.release}")
print(f"Hvilken vetsjon er pc-en på : {my_system.version}")
print(f"Maskin: {my_system.machine}")
print(f"Hvilken type prosesor du har : {my_system.processor}")
print("---------------------------------------------")

#lagring plass på pc-en din  
import psutil
total = int()
used = int()
free = int()
for disk in psutil.disk_partitions():
    if disk.fstype:
        total += int(psutil.disk_usage(disk.mountpoint).total)
        used += int(psutil.disk_usage(disk.mountpoint).used)
        free += int(psutil.disk_usage(disk.mountpoint).free)

print(f"DU HADDE : {round(total / (1024.0 ** 3), 4)} GIGA")
print(f"HVOR MYE DU HAR BRUKT : {round(used / (1024.0 ** 3), 4)} GIGA")
print(f"HVOR MYE DU HAR IGJEN : {round(free / (1024.0 ** 3), 4)} GIGA")
print("---------------------------------------------")

#ip address på den pc
import socket 
h_navn = socket.gethostname()
IP_addres = socket.gethostbyname(h_navn)
print("navn er: " + h_navn)
print("Din ip address er " + IP_addres)
print("---------------------------------------------")

#dine programmer
import subprocess
Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = str(Data)

try:
    for i in range(len(a)):
        print("Du har: ", (a.split("\\r\\r\\n")[6:][i]))

except IndexError as e:
    print("Ferdig se opp")
print("---------------------------------------------")