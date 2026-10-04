tup = (5,1,2,6,3,9,4,8,7)
l1 = []
l2 = []
for i in tup:
    if i%2 == 0:
        l1.append(i)
    else:
        l2.append(i)

tup1 = tuple(l1)
tup2 = tuple(l2)

print(f"Even tuple is {tup1}")
print(f"Odd tuple is {tup2}")