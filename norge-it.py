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
print("Eier navn er: " + h_navn)
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

#strøm på pc-en
import psutil
def convertTime(seconds):
    days = int(seconds / 3600/24)
    seconds = seconds - days*3600*24
    hours = int(seconds / 3600)
    seconds = seconds - hours*3600
    minutes = int(seconds / 60)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
battery = psutil.sensors_battery()
print("Din strøm liv : ", battery.percent)
print("Lader pc-en :", battery.power_plugged)
print("Hvor lenge liv pc-en har :", convertTime(battery.secsleft))
print("---------------------------------------------")
