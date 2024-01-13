from math import sqrt
#Создаём счётчик суммы квадратов
n = 0
#Создаём счётчик квадратов
l = 0
with open ('17_9969.txt') as file_open:
    contents = file_open.read()
    contents = contents.split()
c = len(contents)
for i in range(1, c + 1, 3):
    sq = int(contents[i - 1])
    if sq < 0:
        sq = abs(sq)
    sql = round(sqrt(sq), 2)
    if sql % 100 == 0:
        n += int(sql)
        l += 1
print(l, n)        