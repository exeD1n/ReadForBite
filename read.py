import time

def main(l):
    start = time.time()
    
    with open('myfile3.bin', 'r') as fp:
        chunk = fp.read(l)
        while chunk:
            chunk = fp.read(l)
            
    end = (time.time() - start)
    print(l, 'Байт при считывании программы заняло:', round(end, 3), 'Секунд')
        

if __name__ == '__main__':
    l = [1, 16, 128, 512, 4096, 16384]
    for i in l:
        main(i)
        
