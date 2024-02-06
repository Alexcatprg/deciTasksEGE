S = '8' * 65
while '222' in S or '888' in S:
    if '222' in S:
        S = S.replace('222', '8', 1)
    else:
        S = S.replace('888', '2', 1)
print(S)
#Ответ: 8
