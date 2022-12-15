<<<<<<< Updated upstream
import platform
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
=======
from platform import system, node, release, version, machine, processor 
>>>>>>> Stashed changes
