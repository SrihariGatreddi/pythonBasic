'''def format(first,last):
    f=first.title()
    l=last.title()
    return f'{f} {l}'
formatted=format('srihari','SANAYASI naidu')
print(formatted)'''
def student(*student_data1,**keys1):
    student_info=[]
    for key in keys1:
        for data in student_info:
         student_info+=f'{key}:{data}'
    return student_info
flag=True
while True:
    student_data=[]
    name=input("enetr name:")
    rollno=input("enetr rollno:")
    dept=input("enetr dpt")
    keys=[name,rollno,dept]
    student_data=student(name,rollno,dept,keys1=keys)
    for data in student_data:
      print(data)
    choice=input("want to add more student info?(y/n):")
    if choice=='n':
        flag=False
        