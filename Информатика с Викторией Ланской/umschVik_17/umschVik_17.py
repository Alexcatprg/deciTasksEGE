s = open('17.txt')
red = s.readlines()
for i in range(len(s)):
    red[i] = int(s[i])
count = 0
maxi = 0
for i in range(2, len(red))