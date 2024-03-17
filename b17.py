ngay = int(input('Nhap ngay: '))
thang = int(input('Nhap thang: '))
nam = int(input('Nhap nam: '))
# Giả sử tháng nào cũng là 30 ngày
if(ngay == 1):
    print('Ngay truoc do la {} {} nam 2024'.format(30, thang - 1))
else:
    print('Ngay truoc do la {} {} nam 2024'.format(ngay - 1, thang))