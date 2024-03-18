dem=0
mang = []
mang_nt = []
rong = []
num = int(input('Nhập một số nguyên: '))
for i in range(1, num+1):
    if(num % i == 0):
        dem+=1
        mang_nt.append(i)
    
if(dem==2):
    mang.append(num)
    dem=0
    print('{} bằng {} x {} hoặc bằng {} x {}'.format(num, mang_nt[0], mang_nt[1], mang_nt[1], mang_nt[1]))
else:
    if(dem>2):
        dem=0
        mang_nt= rong
        print('Đây không phải số nguyên tố')