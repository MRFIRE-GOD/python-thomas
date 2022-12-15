import sys
orgi_stdout = sys.stdout
f = open ("save.txt", "w")
sys.stdout = f
for i in range(2):
    print("i = ", i)
sys.stdout = orgi_stdout
f.close