def gcd(m,n):
    if m==0:
        return n
    if n==0:
        return m
    else:
        return gcd(n,m%n)
num1,num2=map(int,input('enter two numbers').split(','))
print(gcd(num1,num2))
