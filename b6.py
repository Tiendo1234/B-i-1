print('Phuong trinh bac hai co dang ax^2 + bx + c (a != 0)')
a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
c = int(input('Nhap c: '))
import math
delta = (b**2) - (4*a*c)
if(delta < 0):
    print('Phuong trinh vo nghiem')
if(delta ==0):
    print('Phuong trinh co nghiem kep: x1 = x2 = {} '.format((-b)/(2*a)))
else:
    print('Phuong trinh co hai nghiem x1 = {}, x2 = {}'.format((-b+math.sqrt(delta))/(2*a), (-b-math.sqrt(delta))/(2*a)))
print(delta)
print((-b)/(2*a))