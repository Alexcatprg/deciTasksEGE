print("w x y z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if ((x <= y) or (z <= w)) and (not (x <= w)):
                    print(w, x, y, z)