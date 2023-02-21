import random

L = []
for i in range(1,10000000):
    L.append(random.randint(1,10000000000000))
f = open('myfile3.bin', 'wb')

# 2.2. Обход списка и запись данных в файл
for item in L:
    # добавить символ '\n', чтобы можно было распознать числа
    s = str(item) + '\n'

    # Метод encode() - конвертирует строку в последовательность байт
    bt = s.encode('utf-8')
    f.write(bt) # метод write() - запись в файл

# 2.3. Закрыть файл
f.close()
