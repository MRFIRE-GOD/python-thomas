import platform
import socket
import subprocess
import shutil
import psutil

hvaErOS=platform.architecture()
hvaEr=platform.node()
hvaErPc=platform.release()
hvaErPcVersjon=platform.version()
hvaErMaskin=platform.machine()
hvaErprosesor=platform.processor()

print(hvaErOS)
print(hvaEr)
print(hvaErPc)
print(hvaErPcVersjon)
print(hvaErMaskin)
print(hvaErprosesor)
print("----------------------------------------------")

#lagring plass på pc-en din
def lagring():
    total = int()
    used = int()
    free = int()
    for disk in psutil.disk_partitions():
        if disk.fstype:
            total += int(psutil.disk_usage(disk.mountpoint).total)
            used += int(psutil.disk_usage(disk.mountpoint).used)
            free += int(psutil.disk_usage(disk.mountpoint).free)

            print(f"Du hadde : {round(total / (1024.0 ** 3), 4)} Giga")
            print(f"Hvor mye du har used : {round(used / (1024.0 ** 3), 4)} Giga")
            print(f"hvor mye du har igjen : {round(free / (1024.0 **3),4)} Giga")



#Ip address
def ip_address():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("pc-navnet er :" + hostname)
    print("Ip address er : " + ip)

#programmer du har
def program():

    Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(Data)

    try:
        for i in range(len(a)):
            print("Du har: ", (a.split("\\r\\r\\n")[6:][i]))

    except IndexError as e:
        print("Ferdig se opp")

lagring()
ip_address()
program()


import json
import exec.fullog as e

inp = e.getdata() #inp now is a dict() which has items, keys and values.

#Query

print('Data collected on:', inp['header']['timestamp'].date())
print('\n CLASS 1 INFO\n')

for item in inp['Demographics']:
    if item['name'] in ['Carly', 'Jane']:
        print(item['name'], 'Height:', item['ht'], 'Age:', item['years'])

for item in inp['Activity']:
    if item['name'] in ['Cycle', 'Run', 'Swim']:
        print(item['name'], 'Athlete:', item['athl_name'], 'Age:', item['years'])