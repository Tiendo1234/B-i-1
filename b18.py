a = int(input('Nhap canh a: '))
b = int(input('Nhap canh b: '))
c = int(input('Nhap canh c: '))
if(a + b <= c) or (a + c <= b) or (b + c <= a):
    print('Khong phai tam giac')
else:
    if(a==b) and (b==c):
        print('Tam giac deu')
    else:
        if((a**2)+(b**2) == c**2) or ((b**2)+(c**2) == a**2) or ((a**2)+(c**2) == b**2):
            print('La tam giac vuong')
        else:
            if(a==b) or (a==c) or (b==c):
                print('La tam giac can')