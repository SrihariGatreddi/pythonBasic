'''year=int(input('enetr the year'))
if year%4==0:
    if year%100==0:
      if year%400==0:
          print('leap year')
      else:
          print('not a leap year')
    else:
        print(' leap year')
else:
    print('not a leap year')'''

year=int(input('enter a year:\n'))
if ((year%4==0 and year%400==0) and (year%100!=0)):
    print('leap year')
else:
    print('not a leap year')