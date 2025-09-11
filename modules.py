# Modules:- (Introduction)

# 1)It is a predefined code.
# 2)in python every file is an Module.
# 3)In Modules its containing all the properties details.


# codes:-

import math
print(math.pi)

import math as m
print(m.pi)

import math as Nani
print(Nani.pi)

# Importing the values into Sum
a=400
b=260
def add(a,b):
    print('sum =',a+b)
def sub(a,b):
    print('rem =',a-b)

add(a,b)
sub(a,b)
print(a)
print(b)
print("Finally Code is Done")        

# Importing datetime module
import datetime
print(datetime.datetime.now())

# Importing sys module
import sys
print(sys.version)

# Importing statistics module
import statistics
data = [10, 20, 30, 40, 50]
print(statistics.mean(data))

# Importing random choices
from random import choice
colors = ["Red", "Blue", "Green"]
print(choice(colors))




