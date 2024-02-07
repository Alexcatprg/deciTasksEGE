'''
Сколько существует семеричных шестизначных чисел, содержащих в своей записи ровно одну цифру 3, в которых при этом
никакие две нечётные цифры не стоят рядом
'''
from itertools import product
col = product('0123456', repeat = 6)
count = 0
for w in col:
    numb = ''.join(w)
    if '3' in numb and all(int(numb[i]) % 2 != int(numb[i + 1]) % 2 for i in range(len(numb) - 1)):
        count += 1
print(count)
#Ответ: 2432