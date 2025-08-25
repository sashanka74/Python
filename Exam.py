print("Welcome to python programming")

print(bin(25))
print(oct(25))
print(hex(25))

print("1234")

number = int(input("Enter your Number"))

if((number % 3 == 0) and (number % 7 == 0)):
    print("Given Number is Divisible by 3 and 7".format(number))
else:
    print("Given Number is Not Divisible by 3 and 7".format(number))

year = 2003
if (year % 400 == 0) and (year % 100 == 0):
    print("it is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("it is a leap year".format(year))
else:
    print("it is not a leap year".format(year))
          
          
marks=int(input('Enter your Marks:'))
if marks>=90:
        print('Excellent')
elif marks>=75 and marks<=89:
        print('Good') 
elif marks>=50 and marks<=74:
        print('Average')   
else:
        print('FAIL')  

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print("")


for i in range(2,101):
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")   
 
str = input("Enter a string: ")
if str == str[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

string = "PythonProgramming"
wordList = string.split()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for word in wordList:
    vowelCount = 0
    for i in range(0, len(word)):
        if word[i] in vowels:
            vowelCount += 1
    print("The word is", word, "and it contains", vowelCount, "vowels in it")





