n = int(input("Nhập n: "))
import math
for c in range(1, n+1):
    for b in range(1, c):
        for a in range(1, b):
            if (a**3) + (b**3) == c**3:
                print("a là {}, b là {}, c là {}".format(a, b, c))
