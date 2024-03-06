'''guess='srihari'
list1=[]
list2=[]
count=0
for i in guess:
    list1.append(i)
    list2.append('-')
    count=count+1
i=1
j=0
while i!=6 or count>=1:
    chance=(input('guess a letter'))
    if chance in list1:
        list2[j]=chance
        j=j+1
        print(list2)
        count=count-1 
    else:
        print(list2)
        i=i+1
if(count==0 and i<6): 
    print('you won')
else:
    print('loss')
        
        '''
display=[]

import random
from hangmanwords import names
choose_word=random.choice(names)
print(choose_word)
for letter in choose_word:
    display+='_'
    
print(display)
exceed=False
count=0
while not exceed and count<6:
    guess=input("enter letter:")
    if guess in display:
            print("alredy guessed the letter")
    for i in range(len(choose_word)):
        letter=choose_word[i]
        if letter==guess and letter not in display:
            display[i]=letter
    print(display)
    if '_' not in display:
        exceed=True
        print('you won')
    if guess not in choose_word:
        count=count+1
        if count==5:
            exceed=True
            print('you loose')

        
    

        
    

