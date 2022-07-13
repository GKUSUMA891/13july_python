


#date and time

#time

import time
result=time.time()
print(result)

#ctime
res=time.ctime(1657691488.9020844)
print(res)   #returns current date and time

# returns time function
res1=help(time.time)
print(res1)

#localtime
res2=time.localtime()
print(res2)#return curent date rime day

#mkitme
a=time.localtime()
b=time.mktime(a)
print(a)

#asctime
c=time.asctime(a)
print(c)
#steftime
print(time.strftime)
x=time.strftime("%d %m %y")
print(x) #exact date

#strptime
'''y="08 August 2022"
s=time.strptime(y,"%d %B %y")
print(s)'''

#datetime
import datetime
res=datetime.datetime(2022,6,13,12,20,34,234)
print(res)

#today
print(datetime.datetime.today())

#now
ver=datetime.datetime.now()
print(ver)

#year,month,day
ver=datetime.datetime.now()
print(ver)
v1=ver.month
v2=ver.day
v3=ver.year
v4=ver.hour
print("month",v1)
print("day:",v2)
print("year:",v3)
print("hour:",v4)

y=time.strftime("%A")
print("%A",y)

z=time.strftime("%a")
print("%a",z)
yy=time.strftime("%B")
print("%B",yy)
ab=time.strftime("%m")
print("%m",y)
y=time.strftime("%Y")
print("%Y",y)
y=time.strftime("%y")
print("%y",y)
y=time.strftime("%p")
print("%p",y)

#date,time
d1=datetime.date(2019,7,5)
d2=datetime.time(12,30,34)
print("time:",d1)
print("date:",d2)

#timedelta
b1=datetime.timedelta(days=20)
b2=datetime.timedelta(days=30)
b3=b1-b2
print("timedelta",b3)
print(type(b3))


import datetime
xx=datetime.datetime.today()
print("%p",xx)


































