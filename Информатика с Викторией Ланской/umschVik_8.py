from itertools import product
col = product('012345678', repeat = 5)
count = 0
for w in col:
    numb = ''.join(w)
    if len(set(numb)) == 5 and 