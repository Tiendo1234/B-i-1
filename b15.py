x = int(input('Nhap x: '))
n = int(input('Nhap n: '))
s = 0
import math
for i in range(1, n+1):
    s += (-1**i) * (x**i)/(math.factorial(i))
print(s)