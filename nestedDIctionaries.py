'''dict1={
    'srihari':{'RollNo':'22981a4241','Subject':'python'},
    'Manikanta':{'RollNo':'22981a4221','Subject':'java','college':'raghu engg college'},
}
print(dict1)
print(dict1['srihari'])
for i in dict1['srihari'].items():
    print(i)
for i,j in dict1['srihari'].items():
    print(f'{i}:{j}')
for student in dict1.keys():
    print(f'{student} Info:')
    for details,value in dict1[student].items():
        print(f'{details}:{value}')
       '''
student=[{'name':'srihari','RollNo':'22981a4241','Subject':'python'},{'name':'manikanta','RollNo':'22981a4221','Subject':'java','college':'raghu engg college'}]
'''print(student[0])
list1=student[0]
print(list1)'''
for i in range(len(student)):
    list1=student[i]
    for keys1,value1 in list1.items():
        print(f"{keys1}:{value1}")
    
          