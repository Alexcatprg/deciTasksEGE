for n in range(4, 10000):
    S = '8' + '4' * n
    while '11' in S or '444' in S or '8888' in S:
        if '11' in S:
            S = S.replace('11', '4', 1)
        if '444' in S:
            S = S.replace('444', '88', 1)
        if '8888' in S:
            S = S.replace('8888', '1', 1)
    print(n)