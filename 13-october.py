#DEFAULT VALUE
from Tools.scripts import var_access_benchmark


def add(a,b=20,c=10):
    print("a= ",a,"b= ",b,"c= ",c)

add(10,10)#it would show b=10 because it will go with global value
"""def add(a,b=20,c)
    print('a= ',a,'b= ',b,'c= ',c)

print(10,10,20) it would show error of syntax if we give two values and make it work for three it would show error"""

a=100
def demo():
    a=10
    print(a)
demo()
print(a)

a=20#b=20
def s():
    global a#to make a local value global use global
    a=30
    #global a must be in the starting otherwise there would be error we cannot allocate a memory
    print("value of a in fn",a)#30 print('value of fn",a,b)
s()
print("value of a outside the fn",a)#30 is printing because we have wriiten global if global not written the it will print 20

#ARBITRARY/VARIABLE LENGTH ARGUMENETS
"""NUMBER OF ARGUMENTS NOT FIXED THAT IT IS NOT FIXED.... FOR ARGUMENTS ALONG WITH * WE MEAN VARIABLE ARGUMENT
THIS IS DONE BY USING STAR IN FN DEF BEFORE THE PARAMETER NAME
EXAMPLE DEF ADD(*A,B)"""

def add(*shreya):
    print("add of variables: ",add)
add(2,3,4,5)

import math
x=int(input())
x=math.radians(x)
print("%.2f"%(math.tan(x)))