for i in range(16):
    t = bin(i)[2:]
    if t.count('1') % 2 == 0:
        print(t)