# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:56:39 2019

@author: mohamed
"""
from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread
temp=1
turn=1
def click(number):
    global buttonList
    global turn
    global temp
    global sc
    if(turn==0):

        buttonList[number]['text']='O'
        buttonList[number]['state']='disable'
        number=str(number)
        sc.send(number.encode('utf-8'))
        turn=1
        check()

def receiveThread(sc):
    global buttonList
    global turn
    global temp
    while True:
        number =sc.recv(300)
        number=number.decode('utf-8')
        number=int(number)
        buttonList[number]['text']='X'
        buttonList[number]['state']='disable'
        turn=0
        check()

def check():
    global turn,temp
    temp+=1
    if(turn==1):
        playerSign='O'
        playerName='player2'
    else:
        playerSign='X'
        playerName='player1'

    b1=btn1['text']
    b2=btn2['text']
    b3=btn3['text']
    b4=btn4['text']
    b5=btn5['text']
    b6=btn6['text']
    b7=btn7['text']
    b8=btn8['text']
    b9=btn9['text']
    
    if(b1==b2 and b2==b3 and b1==playerSign):
        print('gfg')
        messagebox.showinfo(title='congratulation',message='win '+playerName)
    elif(b4==b5 and b5==b6 and b4==playerSign):
        messagebox.showinfo(title='congratulation',message='win '+playerName)
    elif(b7==b8 and b8==b9 and b8==playerSign):
        messagebox.showinfo(title='congratulation',message='win '+playerName)
    elif(b1==b4 and b4==b7 and b4==playerSign):
        messagebox.showinfo(title='congratulation',message='win '+playerName)
    elif(b2==b5 and b5==b8 and b8==playerSign):
        messagebox.showinfo(title='congratulation',message='win '+playerName)
    elif(b3==b6 and b6 ==b9 and b9 ==playerSign):
        messagebox.showinfo(title='congratulation',message='win '+playerName)
    elif(b1==b5 and b5==b9 and b9==playerSign):
        messagebox.showinfo(title='congratulation',message='win '+playerName)
    elif(b3==b5 and b5 ==b7 and b7 == playerSign):
        messagebox.showinfo(title='congratulation',message='win '+playerName)
    if(temp==9):
        messagebox.showinfo(title='congratulation',message='Game Over')
        wind.destroy()

        
sc = socket(AF_INET,SOCK_STREAM)
host ='127.0.0.1'
port=7003
wind = Tk()
wind.title("player2")
wind.geometry("400x300")

player2Lbl  = Label(wind,text=" player2 :O ",font=('helvelt','15'))
player2Lbl.grid(row=0,column=0)

btn1= Button(wind,text=" ",fg="black",bg="yellow",font=("helvelt","15"),width=2,height=1,command=lambda:click(0))
btn1.grid(row=0,column=1)
btn2= Button(wind,text=" ",fg="black",bg="yellow",font=("helvelt","15"),width=2,height=1,command=lambda:click(1))
btn2.grid(row=0,column=2)

btn3= Button(wind,text=" ",fg="black",bg="yellow",font=("helvelt","15"),width=2,height=1,command=lambda:click(2))
btn3.grid(row=0,column=3)

btn4= Button(wind,text=" ",fg="black",bg="yellow",font=("helvelt","15"),width=2,height=1,command=lambda:click(3))
btn4.grid(row=1,column=1)

btn5= Button(wind,text=" ",fg="black",bg="yellow",font=("helvelt","15"),width=2,height=1,command=lambda:click(4))
btn5.grid(row=1,column=2)

btn6= Button(wind,text=" ",fg="black",bg="yellow",font=("helvelt","15"),width=2,height=1,command=lambda:click(5))
btn6.grid(row=1,column=3)

btn7= Button(wind,text=" ",fg="black",bg="yellow",font=("helvelt","15"),width=2,height=1,command=lambda:click(6))
btn7.grid(row=2,column=1)

btn8= Button(wind,text=" ",fg="black",bg="yellow",font=("helvelt","15"),width=2,height=1,command=lambda:click(7))
btn8.grid(row=2,column=2)

btn9= Button(wind,text=" ",fg="black",bg="yellow",font=("helvelt","15"),width=2,height=1,command=lambda:click(8))
btn9.grid(row=2,column=3)
buttonList= list ()
buttonList.append(btn1)
buttonList.append(btn2)
buttonList.append(btn3)
buttonList.append(btn4)
buttonList.append(btn5)
buttonList.append(btn6)
buttonList.append(btn7)
buttonList.append(btn8)
buttonList.append(btn9)
sc.connect((host,port))
th = Thread(target=receiveThread,args=(sc,))
th.start()
wind.mainloop()
