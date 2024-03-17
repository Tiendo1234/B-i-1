n = int(input('Nhap n: '))
tong = 1
k = []
for i in range(1, n):
    tong+=i+1
    if(tong < n):
        k.insert(0, i+1)
print(k[0])