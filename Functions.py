# 1)
def add_numbers(num_list):
    total = 0
    for n in num_list:
        total += n
    return total

numbers = [10, 20, 30, 40, 50]
result = add_numbers(numbers)
print("Total:", result)

# 2)
def check_prime(n):
    if n > 1:
        count = 0
        for i in range (1,n+1):
            if n % i == 0:
                count+=1
    if count == 2:
        print(n,"it is a prime number")
    else:
        print(n,"it is not a prime number")
check_prime(3)
check_prime(6)
check_prime(17)

# 3)
def square(l,b):
    print(l*b)
square(l=5,b=10)

# 4)
def area(l,b,h):
    print(h*l*b)
area(20,6,3)

# 5)
def welcome():
    return'Nani'
print(welcome())

# 6)
def even(n):
    if n%2==0:
        print("even Number")
    else:
        print("odd Number")    
even(11)  
even(8)

# 7)
def check_leap(year):
    if (year % 4 == 0 and year % 100 != 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is Not a Leap Year")
check_leap(2024)
check_leap(2000)
check_leap(2020)






