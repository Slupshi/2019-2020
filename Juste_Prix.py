from math import *
from time import *
from tkinter import *
from random import *
from time import *

n = randint(1, 100)
triche = 1
rtent = 5
timer = 60






def valider():

    global rtent
    global triche
    global timer

    if triche == 1:
        rep.set("TRICHEUR !")
        label1.config(bg="red3")


    if rtent == 0:
        rep.set("C'est perdu !")
        label1.config(bg="red3")
        label3.config(bg="red3")


    if rtent > 0:

        k=int(Ea.get())
        if k > n :
            rep.set("C'est moins !")
        if k < n :
            rep.set("C'est plus !")
        if k==n:
            rep.set("C'est gagné !")
            timer = 100
            label1.config(bg="green")

        rtent= rtent-1
        tent.set("Il te reste "+ str(rtent) + " tentatives")



def start():
    global timer
    timer=60
    triche = 0
    fenp.after(100, compteur)

def compteur():
    global timer
    global triche



    if 61> timer > 0 :
        t.set("Il te reste "+ str(timer) + " secondes")
        timer = timer-1
        fenp.after(1000, compteur)
    elif timer == 0 :
        rep.set("Trop tard !")
        label1.config(bg="red3")
        label4.config(bg="red3")




def reset():
    global timer
    global triche
    global rtent



    rep.set("Reset en cours")
    rep.set("Appuyez sur Start")
    timer = 100
    n = randint(1, 100)
    triche = 1
    rtent = 5
    label1.config(bg="snow4")
    t.set("Il te reste x secondes")
    tent.set("Il te reste "+ str(rtent) + " tentatives")
    label3.config(bg="snow4")
    label4.config(bg="snow4")









fenp = Tk()
fenp.title("Juste Prix")
fenp['bg']='chartreuse3'

rep=StringVar()
rep.set("Appuyez sur Start")
tent=StringVar()
tent.set("Il te reste "+ str(rtent) + " tentatives")
t=StringVar()
t.set("Il te reste x secondes")
label0 = Label(fenp, text='Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100', width =100, height=2 , bg='white',relief='solid').grid(row=1,column=2,columnspan=3)
label1 = Label(fenp, textvariable=rep, width =20, bg='snow4',relief='solid')
label1.grid(row=2,column=3,sticky=S)
label3 = Label(fenp, textvariable=tent, width =20, bg='snow4',relief='solid')
label3.grid(row=2,column=4,sticky=N)
label4 = Label(fenp, textvariable=t, width =20, bg='snow4',relief='solid')
label4.grid(row=2,column=2,sticky=N)

label11 = Label(fenp, text='', width =10, height=20 , bg='chartreuse3').grid(row=1,column=1,rowspan=5)
label12 = Label(fenp, text='', width =10, height=20 , bg='chartreuse3').grid(row=1,column=5,rowspan=5)

bou1 = Button(fenp, text='Valider', width =8, command=valider, bg='snow2',relief='raised').grid(row=3,column=2,columnspan=2,sticky=S)
bou2 = Button(fenp, text='Start', width =8, command=start, bg='snow2',relief='raised').grid(row=4,column=3,columnspan=1,sticky=S)
bou3 = Button(fenp, text='Reset', width =8, command=reset, bg='red3',relief='raised').grid(row=5,column=5,columnspan=1)
Ea=Entry(fenp)
Ea.grid(row=3,column=3,columnspan=1,sticky=S)



fenp.mainloop()