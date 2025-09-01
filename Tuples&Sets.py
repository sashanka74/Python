# ....................................Tuples......................................................
t1=[1,2,3,4]
print(t1)

t2=tuple('nani')
print(t2)

t3={}
print(type(t3))

t2= (12, 5, 9, 21, 3, 15)
print(t2)

print("Minimum:", min(t2))
print("Maximum:", max(t2))

t3 = ("Sashank", 21, "CSE", 8.7)
print("Name:", t3[0])
print("Age:", t3[1])
print("Department:", t3[2])
print("CGPA:", t3[3])

t2=[x for x in range(1,6)]
print(t2)

# ......................................Sets................................................

s1=[1,2,3,4,5,6]
print(s1)

s2=[]
print(type(s2))

s1=[1,2,3,4,5,6]
s1.append(7)
print(s1)

s1.count(s1)
print(s1)

s1.remove(4)
print(s1)

s1.pop()
print(s1)

s1.reverse()
print(s1)

s1=[1,3,5,7,9]
s1.clear()
print(s1)

s6=[1,2,3,4,5,6]
s6=[x for x in range(1,6)]
print(s6)

s1 = {"Nani", "Chinnu"}
s2 = {"Sashank", "Bujji"}
print(s1.union(s2)) 

s1 = {"27", "23"}
s2 = {"11", "22"}
print(s1.difference_update(s2))   

s1 = {"27", "23"}
s2 = {"11", "22"}
print(s1.issubset(s2)) 

s1 = {"27", "23"}
s2 = {"11", "22"}
print(s1.symmetric_difference(s2)) 


