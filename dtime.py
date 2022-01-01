from tkinter import *
import time
 
root = Tk()
time1 = ''
utc=7
clock = Label(root, font=('consolas', 50),fg='lime',bg='black')
#clock.pack(fill=BOTH, expand=1)
root.geometry('300x70')
clock.pack()
def ms() :
    return ((time.time_ns() // 1000000)+(utc*60*60*1000))%(24*60*60*1000)
def dec():
    return str(ms()*100//86400)
def dtime():
    return dec()[0:1]+':'+dec()[1:3]+':'+dec()[3:5]
def tick():
    global time1
    # get the current local time from the PC
    time2 = dtime()
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(100, tick)

tick()


root.config(bg='black')
a=StringVar()
zone=Entry(root,textvariable=a,width=10,bg='black',fg='white')
zone.pack(anchor='w')
root.title('decimal time')
def submit():
    global utc
    utc=int(a.get())
sub_btn=Button(root,text = 'change time zone', command = submit,bg='black',fg='white')
sub_btn.pack(anchor='w')
root.iconbitmap(r'Z:\\bg\\i.ico')
root.mainloop(  )