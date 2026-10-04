list1 = [5,6,9,7,3,6,8,4,5,]

seen = set()
duplicate = set()
for i in list1:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
print(duplicate)