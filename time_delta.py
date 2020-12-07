import datetime

loop=''
while loop='yes':
  print('first date must be smaller then the second one')
  print('give your first input')
  a=int(input('year :  '))
  b=int(input('mounth : '))
  c=int(input('day  :  '))

  print('give your second input')
  e=int(input('year : '))
  f=int(input('mounth : '))
  g=int(input('day : '))

  first_date = datetime.date(a,b,c)
  second_date= datetime.date(e,f,g)

  delta = second_date-first_date

  print(delta.days)
  loop=input('do you wanna run again(yes/no) : ')
