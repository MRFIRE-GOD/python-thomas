import sys    
import platform
import socket
import subprocess
import psutil


import sys

#det her vil gjør outputen lagres i en fil
with open('your-pc-name.txt', 'w') as f:
    sys.stdout = f

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
    print("-------------------------det er info om pc.en----------------------------------------------------------------------------------")


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
        print("---------------------------diskens lagring plass--------------------------------------------------------------------------------")




    #Ip address
    def ip_address():
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print("pc-navnet er :" + hostname)
        print("Ip address er : " + ip)
        print("--------------------------------det er for ip addres---------------------------------------------------------------------------")

    #programmer du har
    def program():

        Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
        a = str(Data)

        try:
            for i in range(len(a)):
                print("Du har: ", (a.split("\\r\\r\\n")[6:][i]))

        except IndexError as e:
            print("Ferdig se opp")
        print("---------------------------------det her viser din programmer som er lasta ned--------------------------------------------------------------------------")


    lagring()
    ip_address()
    program()

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

print("---------------------------------------------")
#this com.. is just to get more in git hub om
