# nested Function
def outer():
    print('hello')
    def inner():
        print('world')
    inner() 
o=outer()
print(o)    

# closer function
def outer():
    a=10
    b=20
    def inner():
        sum=a+b
        print(sum)
    inner()  
outer()     


# Decorator Function 
def decorator(f):
    def wrap():
        print('*' * 10)
        f()
        print('*' * 10)
    return wrap
@decorator
def fun():
    print("hello")
fun()        

# lamda Functions
add=lambda x,y:x+y
print(add(100,500))

# math functions
# 1)
print(abs(-1))
print(abs(-22))
print(abs(496))

# 2)
print(pow(20,4))
print(pow(100,2))
print(pow(33,5))

# 3)
print(round(3.6))
print(round(88.5))
print(round(10))

# 4)
print(divmod(100,2))
print(divmod(88,5))
print(divmod(22,3))

# list functions(max,min)
l1=[23,55,71,2,0]
print(max(l1))
print(min(l1))
    