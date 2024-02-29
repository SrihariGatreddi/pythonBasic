def prime():
    global generator
    for num in range(2,100):
        def primechecker(num):
            count=0
            for i in range(2,num//2+1):
                if num%i==0:
                    count+=1
            if count==0:
                yield num
        generator=primechecker(num)
        for i in generator:
            print(i)
    print(generator)
    for value in generator:
        print(value)
prime()
print(generator)