for a in range(1000):
    if all((x in q) <= (((x in p) and (not(x in a))) <= (not(x in q))) == True for x in range(1000)
        for y in range(1000) for p in range(24, 91) for q in range(47, 116)):
        print()