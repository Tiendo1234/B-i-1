num1 = int(input('Nhap so nguyen duong 1: '))
num2 = int(input('Nhap so nguyen duong 2: '))
uc = []
bc = []
if(num1 > num2):
    for i in range(1, num2+1):
        if(num1 % i == 0) and (num2 % i == 0):
            uc.insert(0, i)
    print(uc[0])
else:
    for i in range(1, num2+1):
        if(num1 % i == 0) and (num2 % i == 0):
            uc.insert(0, i)
    print(uc[0])
while True:
    try:
        if(num1 < num2):
            if(num2 % num1 != 0):
                print("Khong co boi chung")
        if(num2 < num1):
            if(num1 % num2 != 0):
                print("Khong co boi chung")
        else:
            break  
    except ValueError:
        print("Boi chung k la so nguyen")
for i in range(1, (num1*num2)+1):
    if(num1 < num2):
        if(num1*i == num2):
            bc.append(i)
    if(num2<num1):
        if(num1*i == num2):
            bc.append(i)

