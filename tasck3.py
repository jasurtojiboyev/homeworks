num = [1, 3, 3, 5, 5, 5]
num2 = []

for x in num:
    if x not in num2:
        num2.append(x)
print(num2)