from tkinter import *

mestre = Tk()
l = Label(mestre,text="Descobrir Resistência, by Bruno D'avila",fg='green')
l.pack()
frame = Frame(mestre,width=300,height=100)
frame.pack()
l = Label(mestre,text="Tolerância")
l.pack()
e1 = Entry(mestre)
e1.pack()
e1.focus_set()
l = Label(mestre,text="Fator Multiplicador")
l.pack()
e2 = Entry(mestre)
e2.pack()
e2.focus_set()
l = Label(mestre,text="Demais valores")
l.pack()
e3 = Entry(mestre)
e3.pack()
e3.focus_set()
def calc():
    tol = (e1.get())
    mult = int( e2.get())
    resto = int(e3.get())
    Ohms = int(resto * mult)
    w = Message(mestre,text="A resistência é {},tolerância +-{}%".format(Ohms,tol),width=300,fg='red',background='black')
    w.pack()
b = Button(mestre,text="Calcular",command=calc,background='green',fg='white',width=10)
b.pack()
def sair():
    exit()
b = Button(mestre,text='Sair',command=sair,background='red',fg='white',width=10)
b.pack()
mestre.mainloop()









