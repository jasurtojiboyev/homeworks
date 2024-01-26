name =  ["cat", "blue", "skt", "umbrells", "paddy"]
name2 =  ["cat", "blue", "sky", "umbrella", "paddy"]
num = []
for x in name:
    for i in name2:
        if x == i:
            num.append(-1)
        else:
            num.append(1)

print(num)
