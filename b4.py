# la so nguyen duong va co tong cac uoc bang chinh no
while True:
    try:
        num = int(input("Nhập một số nguyên: "))
        if num < 0:
            print("Số bạn nhập vào là số âm. Vui lòng nhập lại số nguyên dương.")
        else:
            break  
    except ValueError:
        print("Vui lòng chỉ nhập số nguyên.")
tong = 0
for i in range(1, num):
    if(num % i == 0):
        tong += i
if(tong == num):
    print('Day la so hoan thien')
else:
    print('Day khong phai so hoan thien')