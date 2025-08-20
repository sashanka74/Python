# loop:-

marks=int(input('Enter your Marks:'))
if marks>35:
    if marks>90:
        print('A grade')
    elif marks>75 and marks<90:
        print('B grade') 
    elif marks>35 and marks<5656:
        print('C grade')   
else:
    if marks>35:
        print('PASS')
    else:
        print('FAIL')                 


# whileloop:-

num=0
while num<10:
    print(num)
    num=num+1
print('Since the loop ended the value is num is:',num)  

# break&continue for loops:-

i=0
while True:
    i+=1
    print(i) 
    if i<10:
        continue
    else:
        break