#exception handling
try:
    x=int(input("enter  value:"))
    print(x)
except ValueError:
    print("except block invalid input")

#multiple exceptions
    import time
try:
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    print("sleep 5 secs")
    time.sleep(5)
    z=x/y
    print(type(z))
except ValueError:
    print("invalid input enter only numbers")
except Exception as arg:
    print("divide by zero exception is  raised")
    print("Error",arg)

#try,except,else
import time
try:
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    z=x*y
    print(z)
except ValueError:
    print("invalid input")
except  ZeroDivisionError:
    print("divisible by zero operand")
except Keyboardinterrupt:
    print("interrupt-cntrlc")
else:
    print("no exception is occured")

#finally
try:
    x=int(input())
    y=int(input())
    print(int(x/y))
except ValueError:
    print("invalid input")
except Exception as arg:
    print(arg)
finally:
    print("no exxceptions")

#nested try,except
try:
    xx=int(input())
    yy=int(input())
    zz=xx%yy
    print(zz)
    try:
        a=input()
        b=input()
        c=a+b
        print(c)
    finally:
        print("invalid input")
except ValueError:
    print("invalid input")
finally:
    print("no  exceptions")
    
try:
 file = open("testfile", "r")
 file.write("This is my test file for exception handling!!")
except IOError:
 print ("Error: can\'t find file or read data")
else:
 print ("Written content in the file successfully")


#finnally
try:
 file = open("testfile", "w")
 file.write("This is my test file for exception handling!!")
finally:
 print ("Error: can\'t find file or read data")
 file.close()

#try,finnally,clause
try:
    file = open("testfile", "w")
    try:
        file.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
    file.close()
except IOError:
    print("Error: can\'t find file or read data")
    
# Define a function here.
def temp_convert(var):
    try:
        returnint(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\n",Argument)

#user defined exceptions
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


