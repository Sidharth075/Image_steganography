import tkinter
from tkinter import *
from tkinter import filedialog
import tkinter as tk
#from tkFileDialog import askopenfilename
from PIL import Image,ImageTk
import os
from stegano import lsb
root=Tk()
root.title("STEGANOGRAPHY")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#ec2131")
def showimage():
    global filename
    filename=filedialog.askopenfilename(intialdir=os.getcwd(),title="Select Image File",filetype=[("PNG file","*.png"),("Jpg File","*.jpg"),("All file","*.txt")])
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
def Hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)

def Show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)

def save():
    secret.save("hidden.png")
    

#icon
image_icon = ImageTk.PhotoImage(Image.open("board.jpg"))
root.iconphoto(False,image_icon)

#logo
logo=ImageTk.PhotoImage(Image.open("box.png"))
Label(root,image=logo,bg="red").place(x=10,y=10)

Label(root,text="SECRET MESSAGE",bg="blue",fg="white",font="italic 20 bold").place(x=100,y=20)

#first Frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

#second Frame
frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third Frame
frame3=Frame(root,bd=3,bg="black",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="OPEN IMAGE",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="CLOSE IMAGE",width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=30)
Label(frame3,text="Picture,Image,Photo File",bg="white",fg="yellow").place(x=20,y=5)

#fourth Frame
frame4=Frame(root,bd=3,bg="green",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="HIDE DATA",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="SHOW DATA",width=10,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="Picture,Image,Photo File",bg="pink",fg="yellow").place(x=20,y=5)


root.mainloop()
