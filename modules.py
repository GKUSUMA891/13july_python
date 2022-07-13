#modules
#div.py
import mod1 as dv
division=dv.div(12,30)
print(division)

 #multiple.py
import mod1 as mu
multiplication=mu.mul(10,20)
print(multiplication)


#sub.py
import mod1 as su
subtraction=su.sub(20,15)
print(subtraction)


#addition.py
import mod1 as md
addition=md.add(10,25)
print(addition)

#mod1.py
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

#module
def greeting(name):
    print("Hai", + name)
#import
    
import mymodules
mymodules.greeting("hello world")

person1={"name":"john","age":36,"country":"usa"}

a=mymodules.person1["age"]
print(a)

#re-naming
import mymodules as mx
a=mx.preson1["age"]
print(a)

#built_in_funnctions
#platform module
import platform
x=platform.ststem()
pritn(x)

#using dir function
import platform
x=dir(platform)
print(x)

#imoort from module
def greeting(name):
    print("hello, " +name)

person1={"name":"john","age":36,"country":"usa"}

from mymodules import person1
print(person["age"])

