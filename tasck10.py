royxat = [7, 3, 5, 1]
n = int(input("son kriting :"))

if len(royxat) < n:
    print(None)
else:
    tartibga_soladi = sorted(royxat)
    natija = tartibga_soladi[n - 1]
    print(natija)
