a1 = float(input('Nhap a1: '))
b1 = float(input('Nhap b1: '))
c1 = float(input('Nhap c1: '))
a2 = float(input('Nhap a2: '))
b2 = float(input('Nhap b2: '))
c2 = float(input('Nhap c2: '))
dinh_thuc = (a1*b2) - (b1*a2)
dinh_thuc_x = (c1*b2) - (c2*b1)
dinh_thuc_y = (c2*a1) - (c1*a2)
if(dinh_thuc == 0):
    print('He phuong trinh co vo so nghiem')
else:
    print('Nghiem x la: {}'.format(dinh_thuc_x/dinh_thuc))
    print('Nghiem y la: {}'.format(dinh_thuc_y/dinh_thuc))
if(dinh_thuc_y == dinh_thuc_x == 0):
    print('HPT co vo so nghiem')
else:
    if(dinh_thuc_y == 0) or (dinh_thuc_x == 0):
        print('HPT vo nghiem')