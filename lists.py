'''list=[10,12,'srihari Gatreddi',45,'srihrai','63922981a4241']
print(list)
print(list[0])
print([list[1]])
print(list[2])
print(list[:])
print(list[:len(list)])
print(list[0:])
'''
# input a list
# m1
'''string=input("enter a string")
list=string.split()
print(list)'''
#m2
'''n=int(input('enetr size of the list'))
list=list(map(int,input('enetr list items').split()))[:n]
print(list)
'''
#m3
'''n=int(input('enter size'))
list=[]
for i in range(0,n):
    list.append(int(input()))
print(list)'''
#m4 exceptional handling
'''try:
    my_list=[]
    while True:
        my_list.append(int(input()))
except:
    print(my_list)
        
        '''
#nested lists
x=int(input('enter'))
y=int(input('enter'))
outerlist=[]
innerlist=[]
for i in range(x):
    for j in range(y):
        innerlist.append(input())
    outerlist.append(innerlist)
    innerlist=[]
print(outerlist)