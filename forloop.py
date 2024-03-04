heights=input("eneter heights seperated by spqace:")
list=heights.split()
count=0
for j in list:
    count=count+1
for i in range(0,count):
    list[i]=int(list[i])
print(list)
sum=0
for height in list:
    sum=sum+height
print(sum)
avg=round(sum/count)
print(avg)

    