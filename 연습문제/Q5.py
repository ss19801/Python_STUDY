def fibo(n):
    if n==0: return 0
    if n==1: return 1
    return fibo(n-2)+fibo(n-1)

num=int(input())

for i in range(num):
    print(fibo(i))

