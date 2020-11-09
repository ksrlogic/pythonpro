from tkinter import *
from tkinter import messagebox

def python_show():
    print('학번: %s'%in1.get())
    print('이름: %s'%in2.get())
    print('나이: %s'%int(in3.get()))

def mbox_show():
    messagebox.showinfo('학생정보출력', '학번: %s\n이름: %s \n, 나이: %d'%(in1.get(),in2.get(),int(in3.get())))

sinfo = Tk()

sinfo.title("학생 정보 입력")
sinfo.geometry("300x100+150+150")

Label(sinfo, text="학 번").grid(row=0)
Label(sinfo, text="이 름").grid(row=1)
Label(sinfo, text="나 이").grid(row=2)

in1 = Entry(sinfo, width=15)
in2 = Entry(sinfo, width=15)
in3 = Entry(sinfo, width=15)

in1.grid(row=0, column=1)
in2.grid(row=1, column=1)
in3.grid(row=2, column=1)

Button(sinfo, text="파이선창", padx=15, bg='deepskyblue',
       command = python_show).grid(row=3, column=0)

Button(sinfo, text="메세지박스", padx=15, bg='deepskyblue',
       command = mbox_show).grid(row=3, column=1, sticky=W)

Button(sinfo, text="종료", padx=15, bg='tomato',
        command= sinfo.destroy).grid(row=3, column=2)

sinfo.mainloop()