from tkinter import *

months = {1:31,
          2:28,
          3:31,
          4:30,
          5:31,
          6:30,
          7:31,
          8:31,
          9:30,
          10:31,
          11:30,
          12:31
          }

month_lis = [31,28,31,30,31,30,31,31,30,31,30,31,0,0]

def root_cc():
    root_c = Tk()
    Label(root_c,text='input error!!!!!! please check your input',
          fg='red',pady=50,padx=10).pack()
    root_c.mainloop()

#leap year testing
def leap(year):
    if year%4==0:
        months[2]=29
        month_lis[1]=29
    else:
        months[2]=28
        month_lis[1]=28

def is_leap(year):
    if year%4==0:
        return True
    else:
        return False

def lis_num(a,b):
    global num_lis
    num_lis = []
    for i in range(1,b-a):
        num_lis.append(a+i)
    

def count():
    dates = {}
    dates['day_1']=int(self_1.entry1.get())
    dates['mnth_1']=int(self_1.entry2.get())
    dates['yr_1']=int(self_1.entry3.get())
    dates['day_2']=int(self_2.entry1.get())
    dates['mnth_2']=int(self_2.entry2.get())
    dates['yr_2']=int(self_2.entry3.get())

    total_days = 1
        
    if dates['yr_1'] > dates['yr_2'] :
        root_cc()

    if dates['yr_1'] == dates['yr_2'] :
        leap(dates['yr_1'])
        if dates['mnth_1'] > dates['mnth_2']:
            root_cc()
        if dates['mnth_1'] == dates['mnth_2']:
            if dates['day_1']>dates['day_2']:
                root_cc()
            else:
                total_days += dates['day_2'] - dates['day_1']
        else:
            total_days += months[dates['mnth_1']] - dates['day_1']
            lis_num(dates['mnth_1'],dates['mnth_2'])
            for i in num_lis:
                total_days+= months[i]
            total_days += dates['day_2']

    else:
        leap(dates['yr_1'])
        total_days += months[dates['mnth_1']] - dates['day_1']
        for i in month_lis[dates['mnth_1']:]:
            total_days += i

        lis_num(dates['yr_1'],dates['yr_2'])
        for i in num_lis:
            if is_leap(i)==True:
                total_days +=366
            else:
                total_days +=365
                
        leap(dates['yr_2'])
        total_days+=dates['day_2']
        if dates['mnth_2']!=1:
            for i in month_lis[:dates['mnth_2']-1]:
                total_days +=i

    root_as = Tk()
    Label(root_as,
          text='the total number of days are :  '+str(total_days),
          fg='blue',pady=70,padx=20).pack()

    root_as.mainloop()
            
            
            
        
            
root=Tk()
root.title('day count app')


label1 =Label(root,text='enter your frist and sencond date')
label1.grid(row=0,column=0)
label2 = Label(root,text='frist date :  ')
label2.grid(row=1,column=0)
x=2


class lab:
    def labels_(self):
        global x
        global entry1
        global entry2
        global entry3
        label3 = Label(root,text='day : ')
        label3.grid(row=x,column=0)
        self.entry1 = Entry(root,width=10)
        self.entry1.grid(row=x,column=1,pady=10)

        label4 = Label(root,text='mounth : ')
        label4.grid(row=x,column=2)
        self.entry2 = Entry(root,width=10)
        self.entry2.grid(row=x,column=3,pady=10)

        label5 = Label(root,text='year : ')
        label5.grid(row=x,column=4)
        self.entry3 = Entry(root,width=20)
        self.entry3.grid(row=x,column=5,pady=10,padx=5)


self_1 = lab()
self_2 = lab()

self_1.labels_()
label6 = Label(root,text='second date :  ')
label6.grid(row=4,column=0)
x=5
self_2.labels_()

button = Button(root,text='count day',command=count)
button.grid(row=7,column=3,pady=10)

root.mainloop()
