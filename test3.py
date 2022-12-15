
import psutil

hdd = psutil.disk_usage('/')

print ("Total: %d GiB" % hdd.total / (2**30))
print ("Used: %d GiB" % hdd.used / (2**30))
print ("Free: %d GiB" % hdd.free / (2**30))

import os

def get_machine_storage():
    result=os.statvfs('/')
    block_size=result.f_frsize
    total_blocks=result.f_blocks
    free_blocks=result.f_bfree
    # giga=1024*1024*1024
    giga=1000*1000*1000
    total_size=total_blocks*block_size/giga
    free_size=free_blocks*block_size/giga
    print('total_size = %s' % total_size)
    print('free_size = %s' % free_size)

get_machine_storage()