def F(n):
    if n == 1:
        return n
    else:
        return n - 1 + F(n + 1)


print(F(2028))