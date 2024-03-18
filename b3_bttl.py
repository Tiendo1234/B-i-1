mang_ban_dau = []
mang_nt = []
mang_cp = []
dem=0
dem1=0
num = int(input('nhap n: '))
for i in range(num):
    so = int(input('Nhap so bat ky: '))
    mang_ban_dau.append(so)
for a in mang_ban_dau:
    for i in range(1, a+1):
        if(a % i == 0):
            dem+=1
    if(dem==2):
        mang_nt.append(a)
        dem=0
    else: 
        if(dem>2):
            dem=0
for b in mang_ban_dau:
    for i in range(1, b+1):
        if(i*i == b):
            dem1+=1
    if(dem1==1):
        mang_cp.append(b)
        dem1=0
print(mang_ban_dau)
print(mang_nt)
print(mang_cp)
