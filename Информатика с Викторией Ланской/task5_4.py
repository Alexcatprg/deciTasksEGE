res = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += s[-2:]
    else:
        s = list(s)
        s.insert(0, '1')
        s.append('0')
        s = str(s)
    if int(s, 2) > 410:
        res.append(int(s, 2))
print(min(res))
# Выдаёт ошибку ValueError: invalid literal for int() with base 2: "['1', '1', '0']"