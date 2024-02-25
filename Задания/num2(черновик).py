s = [int(x) for x in open('zad17_2023 для вариантов.txt')]
maxi = max(x for x in s)
res = []
count = 0
for i in range(len(s) - 2):
    if s[i] % 7 == 0 or s[i + 1] % 7 == 0:
        res.append(s[i] + s[i + 1])
        count += 1
print(count, max(res))