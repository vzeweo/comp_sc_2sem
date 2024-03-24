from math import*
t= float(input("Введите t:"))
a=2*t**2
b=(3*t-2)
c=2*t-3
if a==0:
    x-c/b
    print('x=',x)
else:
    D=b**2-4*a*b*c
    print("D:",D)
    print("a:",a)
    print("b:",b)
    print("c:",c)
    if D>=0:
        x1= (-b + math.sqrt(0))/(2*a)
        x2= (-b - math.sqrt(0))/(2*a)
        print('x1=:', x1, 'x2=',x2)
    else:
        print("D<0")