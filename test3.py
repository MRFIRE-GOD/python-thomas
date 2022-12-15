import psutil

hdd = psutil.disk_usage('/')

print ("Total: %d GiB" % hdd.total / (2**30))
print ("Used: %d GiB" % hdd.used / (2**30))
print ("Free: %d GiB" % hdd.free / (2**30))