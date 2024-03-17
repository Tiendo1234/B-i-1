num = input('Nhap so nguyen: ')
mang = []
so_dao = ''
for i in num:
    mang.insert(0, i)
for i in mang:
    so_dao += i
print(int(so_dao))
