import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from calm import Calm
from depressed import Depressed
from enlightenment import Enlightenment
from happy import Happy
from sad import Sad

class Face_Recognition_System:
    def __init__(self, root):
         self.root = root
         self.root.geometry("1530x790+0+0")
         self.root.title("***Music***")
         
         #bgImage
         img3=Image.open(r"C:\Users\hp\Desktop\Adi_college\Mini Project_TE\mp_music\Images\bg.jpeg")
         img3=img3.resize((1530,790),Image.ANTIALIAS)
         self.photoimg3=ImageTk.PhotoImage(img3)
         
         bg_image=Label(self.root,image=self.photoimg3)
         bg_image.place(x=0,y=0,width=1530,height=790)

         title_lbl=Label(bg_image,text="Select Your Mood",font=("Playfair Display",35,"bold"),bg="LightGoldenRod1",fg="midnight blue")
         title_lbl.place(x=0,y=0,width=1530,height=45)
         
         #Enlightment Button
         img4=Image.open(r"C:\Users\hp\Desktop\Adi_college\Mini Project_TE\mp_music\Images\En.jpeg")
         img4=img4.resize((220,220),Image.ANTIALIAS)
         self.photoimg4=ImageTk.PhotoImage(img4)

         b1=Button(bg_image,image=self.photoimg4,cursor="hand2",command=self.enlightenment_mood)
         b1.place(x=200,y=100,width=220,height=220)

         b1_1=Button(bg_image,text="Enlightenment",cursor="hand2",command=self.enlightenment_mood,font=("cinzel",15,"bold"),bg="cadetBlue1",fg="grey1")
         b1_1.place(x=200,y=300,width=220,height=40)
         
         #Happy Button
         img8=Image.open(r"C:\Users\hp\Desktop\Adi_college\Mini Project_TE\mp_music\Images\Happy.jpeg")
         img8=img8.resize((220,220),Image.ANTIALIAS)
         self.photoimg8=ImageTk.PhotoImage(img8)

         b1=Button(bg_image,image=self.photoimg8,cursor="hand2",command=self.happy_mood)
         b1.place(x=200,y=380,width=220,height=220)

         b1_1=Button(bg_image,text="Joy",cursor="hand2",command=self.happy_mood,font=("cinzel",15,"bold"),bg="cadetBlue1",fg="grey1")
         b1_1.place(x=200,y=580,width=220,height=40)
         
         #Calm Button
         img5=Image.open(r"C:\Users\hp\Desktop\Adi_college\Mini Project_TE\mp_music\Images\calm.jpeg")
         img5=img5.resize((220,220),Image.ANTIALIAS)
         self.photoimg5=ImageTk.PhotoImage(img5)

         b1=Button(bg_image,image=self.photoimg5,cursor="hand2",command=self.calm_mood)
         b1.place(x=650,y=200,width=220,height=220)

         b1_1=Button(bg_image,text="Anticipation",cursor="hand2",command=self.calm_mood,font=("cinzel",15,"bold"),bg="cadetBlue1",fg="grey1")
         b1_1.place(x=650,y=400,width=220,height=40)
         
          #Sad  Button
         img6=Image.open(r"C:\Users\hp\Desktop\Adi_college\Mini Project_TE\mp_music\Images\sad.jpeg")
         img6=img6.resize((220,220),Image.ANTIALIAS)
         self.photoimg6=ImageTk.PhotoImage(img6)

         b1=Button(bg_image,image=self.photoimg6,cursor="hand2",command=self.sad_mood)
         b1.place(x=1100,y=100,width=220,height=220)

         
         b1_1=Button(bg_image,text="Sad",cursor="hand2",command=self.sad_mood,font=("cinzel",15,"bold"),bg="cadetBlue1",fg="grey1")
         b1_1.place(x=1100,y=300,width=220,height=40)

          #Depressed Button
         img11=Image.open(r"C:\Users\hp\Desktop\Adi_college\Mini Project_TE\mp_music\Images\Depressed.jpeg")
         img11=img11.resize((220,220),Image.ANTIALIAS)
         self.photoimg11=ImageTk.PhotoImage(img11)

         b1=Button(bg_image,image=self.photoimg11,cursor="hand2",command=self.depressed_mood)
         b1.place(x=1100,y=380,width=220,height=220)

         b1_1=Button(bg_image,text="Depressed",cursor="hand2",command=self.depressed_mood,font=("cinzel",15,"bold"),bg="cadetBlue1",fg="grey1")
         b1_1.place(x=1100,y=580,width=220,height=40)

#_________________Funtion Buttons___________________
    def enlightenment_mood(self):
        a=random.randint(501, 700)
        print(a)
        self.new_window=Toplevel(self.root)
        self.app=Enlightenment(self.new_window)
        
    def happy_mood(self):
        b=random.randint(311,500)
        print(b)
        self.new_window=Toplevel(self.root)
        self.app=Happy(self.new_window)
        
    def calm_mood(self):
        c=random.randint(175, 310)
        print(c)
        self.new_window=Toplevel(self.root)
        self.app=Calm(self.new_window)
        
    def sad_mood(self):
        d=random.randint(76, 150)
        print(d)
        self.new_window=Toplevel(self.root)
        self.app=Sad(self.new_window)
        
    def depressed_mood(self):
        e=random.randint(10, 75)
        print(e)
        self.new_window=Toplevel(self.root)
        self.app=Depressed(self.new_window)
        
         
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()