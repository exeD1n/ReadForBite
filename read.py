import time

def main(i):
    start = time.time()
    
    with open('myfile3.bin', 'r') as fp:
        chunk = fp.read(i)
        while chunk:
            chunk = fp.read(i)
            
    end = (time.time() - start)
    print(i, 'Байт при считывании программы заняло:', round(end, 3), 'Секунд')
        

if __name__ == '__main__':
    l = [1, 16, 128, 512, 4096, 16384]
    for i in l:
        main(i)
        
