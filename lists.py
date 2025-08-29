# lists

l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l1.append(6)
print(l1)

l1.extend([7,8,9,10])
print(l1)

l2=l1.copy()
print(l2)

l2.insert(3,200)
print(l2)

l2.remove(9)
print(l2)

l1.pop()
print(l1)

l1.clear()
print(l1)

l3=[22,33,44]
del(l3)

# methods in list

l1=[2,3,4,5,6,3]
print(l1.index(3))

print(l1.count(3))

l1.reverse()
print(l1)

l5=[34,21,99,24,65,11,0,17]
l5.sort()
print(l5)

# nested list

nl=[(100,200,300),(150,250,350),(120,220,320)]
for x in nl:
    print(x)

nl=[(2,1,3),(3,2,1),(4,5,3)]  
for y in nl:
    print(y)  