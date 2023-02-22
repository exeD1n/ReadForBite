import random

L = []
for i in range(1,10000000):
    L.append(random.randint(1,10000000000000))
f = open('myfile3.bin', 'wb')

for item in L:
    s = str(item) + '\n'
    bt = s.encode('utf-8')
    f.write(bt)
    
f.close()
