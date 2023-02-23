from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2

class Depressed:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("**Depressed**")
        
if __name__== "__main__":
        root=Tk()
        obj=Depressed(root)
        root.mainloop()  
        