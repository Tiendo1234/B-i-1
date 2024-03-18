dem=0
num = [int(input('Nhap so nguyen to: '))]
for i in range(1, num+1):
    if(num%i == 0):
        dem+=1
if(dem==2):
    print('day la so nguyen to')
else: 
    print('day khong la so nguyen to')
