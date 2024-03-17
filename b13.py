n = int(input('nhap n'))
s = 1
data = 1
for i in range(1, n):
    data *= (i+1)
    s += data
print(s)

