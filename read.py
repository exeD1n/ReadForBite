import time 

start = time.time()

#1, 16, 128, 512, 4096 и 16384 байт
with open('myfile3.bin', 'r') as fp:
    # читаем файл по 20 байт
    chunk = fp.read(16384)
    while chunk:
        print(chunk)
        chunk = fp.read(16384)
        
end = (time.time() - start)/60
print(end)