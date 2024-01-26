get = {
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}
get2 = []
for x in get.values():
    get2.append(x)
    get2.sort()
j = ", " .join(get2)
print(get2)

