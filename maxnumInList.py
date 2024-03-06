n=int(input("enter number of items:"))
list1=list(map(int,input("Enter list items:").strip().split()))[:n]
print(list1)
max_num=list1[0]
for i in range(1,n):
    if list1[i]>max_num:
        max_num=list1[i]
print(max_num)
    