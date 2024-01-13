'''
1. Строится двоичная запись числа N.

2. Далее эта запись обрабатывается по следующему правилу:
а) если число N делится на 3, то к этой записи дописываются
три последние двоичные цифры;
б) если число N на 3 не делится, то остаток от деления умножается на 3,
переводится в двоичную запись и дописывается в конец числа.
Полученная таким образом запись является двоичной записью искомого
числа R.

3. Результат переводится в десятичную систему и выводится на экран.
Например, для исходного числа 12 = 11002 результатом является число
11001002 = 100, а для исходного числа 4 = 1002 это число 100112 = 19.
Укажите минимальное число R, большее 151, которое может быть получено
с помощью описанного алгоритма. В ответе запишите это число
в десятичной системе счисления.
'''
res = []#создаём список
for n in range(1, 1000):
    s = bin(n)[2:]#строится двоичная запись числа
    if n % 3 == 0:#если число делится на 3 , то к этой записи дописываются
        s += s[-3:]#три последние двоичные цифры
    else:#в противном случае остаток от деления на 3 умножается на 3,
        s += bin(n % 3 * 3)[2:]#переводится в двоичную запись и добавляется в конец числа
    if int(s, 2) > 151:#переводим в десятичную систему счисления
        res.append(int(s, 2))
print(min(res))#выводится минимальное число, которое больше 151      