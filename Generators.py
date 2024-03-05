'''def fib(limit): 
      
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number 
    while a < limit: 
        yield a 
        a, b = b, a + b 
  
# Create a generator object 
x=fib(5) 
  
# Iterating over the generator object using next 
# In Python 3, __next__()
  
# Iterating over the generator object using for 
# in loop. 
print("\nUsing for in loop") 
for i in x:  
    print(i)
print(x)'''
#python generator expression:
'''generator=(i for i in range(11) if i%2==0)
print(generator)
for value1 in generator:
    print(value1)
print(generator)
'''
'''def prime(num):
    count=0
    for i in range(2,(num//2)+1):
        if num%i==0:
            count+=1
    if count==0:
        return 1
    else:
        return 0
genetaor1=(i for i in range(10)  if prime(i))
for i in genetaor1:
    print(i)'''
    
