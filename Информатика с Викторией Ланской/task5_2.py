res = []
for n in range(1, 1000):
    s = bin(n)[2:]
    s += s[0]
    ed = s.count('1')
    if ed % 2 == 0:
        s += '0'
    else:
        s += '1'
    ed = s.count('1')
    while ed % 2 == 0:
        s += '1'
        ed = s.count('1')
    if int(s, 2) > 2222:
        res.append(int(s, 2))
print(min(res))
# Ответ: 2223 (Наталье Фёдоровне)