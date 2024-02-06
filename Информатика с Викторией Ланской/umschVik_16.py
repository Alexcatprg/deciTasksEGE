def F(n):
    if n == 1:
        return n
    if n > 1:
        return n - 1 + F(n - 1)

print(F(2028) - F(2024))
#Выдаёт ошибку
