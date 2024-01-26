num = ["1010101010101"]
m = []
for x in num:
    for y in x:
        if y == "1":
            m.append(True)
        else:
            m.append(False)
print(m)
