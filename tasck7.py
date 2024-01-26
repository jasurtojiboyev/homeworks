num = [[4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]]

umumiy_hajm = 0
for x in num:
    uzunlik, kenglik, balandlik = x
    umumiy_hajm += uzunlik * kenglik * balandlik

print(f"Barcha birlashtirilgan qutilar umumiy hajmi: {umumiy_hajm}")