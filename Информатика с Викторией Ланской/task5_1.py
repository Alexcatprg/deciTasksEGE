res = []
for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += '10'
    else:
        s += '01'
    if int(s, 2) > 222:
        res.append(int(s, 2))
print(min(res))
# Ответ: 226(Наталье Фёдоровне)