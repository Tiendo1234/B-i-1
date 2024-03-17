chuoi = input('Nhap chuoi: ')
dem = 0
for i in chuoi:
    if(i ==' ') or (i == ',') or (i == '.'):
        dem+=0
    else:
        dem+=1
print('So ky tu trong chuoi la: ', dem)
print(chuoi.title())