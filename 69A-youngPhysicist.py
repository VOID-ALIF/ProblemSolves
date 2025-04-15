# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    x_sum, y_sum, z_sum = 0, 0, 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        x_sum += x
        y_sum += y
        z_sum += z
    if x_sum == 0 and y_sum == 0 and z_sum == 0:
        print("YES")
    else:
        print("NO")

solve()