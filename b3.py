num = int(input('Nhap so nguyen: '))
dem = 0
for i in range(1, num+1):
    if(num % i == 0):
        dem+=1
if(dem==2):
    dem=0
    print('Day la so nguyen to')
if(dem>2):
    dem=0
    print('Day khong la so nguyen to')