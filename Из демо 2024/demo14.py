print('1 тип')
alph = '0123456789ABCDEFGHI' # создаём переменную - алфавит
for x in alph:
    f = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if f % 18 == 0:
        print(f // 18)

print('2 тип')
f = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
count = 0
while f:
    if f % 25 == 0:
        count += 1
    f //= 25
print(count)