from tkinter import *

def pic1():
    label1.config(image=photo1)
    label2.config(fg='green')

def pic2():
    label1.config(image=photo2)
    label2.config(fg='red')

ps = Tk()

ps.title('남극 펭! 빼어날 수!')

photo = PhotoImage(file='pengsoo.png')
label1 = Label(ps, image=photo)

photo1 = PhotoImage(file='peng1.png')
photo2 = PhotoImage(file='peng2.png')

msg = '펭하! 펭수를 보아라-행복해질것이니-펭러뷰!!!'

label2 = Label(ps, text=msg, font=('맑은 고딕', 14), fg='blue')

btn1 = Button(ps, text='펭하', width=20, font=('' ,16), bg='olivedrab', command=pic1)
btn2 = Button(ps, text='펭러브', width=20, font=('', 16), bg='orangered', command=pic2)

label1.pack(side=TOP)
label2.pack(side=TOP)
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)
ps.mainloop()