# ...............................Dictionary.......................................................

d1= {'name':('Nani'),'age':(22),'location':('Hyderabad')}
print(d1)

for i in d1['name']:
    print(i)

d2={1:'one',2:'two',3:'three'}     #representing the key value pairs
print(d2)

d3={1:'Nani'}
d4={2:'Male'}
d5={3:'2003'}
d6={}
print(d3,d4,d5,)

d2[1]='Nani'                       #changing of values
print(d2)

d4[2]='Gender-Male'                #changing of values
print(d4)

d6[4]='Sashank'                    #adding the key & value pairs
print(d6)

# ..............................Dictionary-Ways................................................

#..........1)iterable Pairs:-

l1=[['Movie','RRR'],['Hero-Name','NTR'],['heroin','Alia'],['Director','SS Jakkanna']]
d1=dict(l1)
print(d1)                 #Lists to Lists

l1=[('Movie','RRR'),('Hero-Name','NTR'),('heroin','Alia'),('Director','SS Jakkanna')]
d1=dict(l1)
print(d1)                 #lists to tuples

l1=(['Movie','RRR'],['Hero-Name','NTR'],['heroin','Alia'],['Director','SS Jakkanna'])
d1=dict(l1)
print(d1)                  #tuples to lists

l1=(('Movie','RRR'),('Hero-Name','NTR'),('heroin','Alia'),('Director','SS Jakkanna'))
d1=dict(l1)
print(d1)                  #tuples to tuples

l1=(('Movie','RRR'),('Hero-Name','NTR'),('heroin','Alia'),('Director','SS Jakkanna'))
d1=dict(l1)
for x in d1.items():
    print(x)

for i in d1.keys():
    print(i)  

for i in d1.values():
    print(i)                #representing in separate ways

#..........2)Zip values:-

l2=['First Name','Last Name','Age','Gender']
l3=['Nani','Gattamaneni','22','Male']
d1=dict(zip(l2,l3))
print(d1)                       #zip of lists

l2=['First Name','Last Name','Age','Gender']
l3=['Nani','Gattamaneni','22','Male']
d1=dict(zip(l2,l3))
for i in d1.keys():
    print(i)                    #keys

l2=['First Name','Last Name','Age','Gender']
l3=['Nani','Gattamaneni','22','Male']
d1=dict(zip(l2,l3))
for i in d1.values():
    print(i)                    #values

l2=['First Name','Last Name','Age','Gender']
l3=['Nani','Gattamaneni','22','Male']
d1=dict(zip(l2,l3))
for x in d1.items():
    print(x)                    #items

#...........3)Enumarated Values:-

l3=['one','two','three','four']
d4=dict(enumerate(l3,start=3))
print(d4)

l2=[2,3,4,5,6]
d3=dict(enumerate(l2,start=4))
print(d3)

l1=[2000,2001,2002,2003]
d2=dict(enumerate(l1,start=0))
print(d2)



