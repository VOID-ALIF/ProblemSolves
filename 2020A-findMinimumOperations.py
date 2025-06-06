# Author : AlifSrSE
# Date : 2025-03-02
# Problem link : https://codeforces.com/contest/2020/problem/A

def min_operations(n, k):
    if k == 1:
        return n 
    operations = 0
    while n > 0:
        operations += n % k  
        n //= k  
    return operations
t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    results.append(min_operations(n, k))
for result in results:
    print(result)