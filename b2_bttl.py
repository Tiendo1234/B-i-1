import math
dem=0
num = int(input('nhap so nguyen duong: '))
for i in range(1, num+1):
    if(i*i == num):
        dem+=1
if(dem == 1):
    print('Day la so chinh phuong')
else:
    print('Day khong la so chinh phuong')
