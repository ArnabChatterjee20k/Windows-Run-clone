import tkinter as tk,os,csv
from tkinter.constants import END
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image
from tkinter.messagebox import showerror
from tkinter import StringVar, ttk, filedialog as fd

class Win(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #configure root window
        self.title("Run Clone")

        # Tk().geometry("widthxheight+Left+Top")
        self.geometry("400x160+10+600")
        self.resizable(False,False)
        self.iconbitmap("run.ico")
        
        #intro
        #placing resized image on a label
        image=Image.open("run.jpg")
        img=image.resize((30,30))
        self.my_img=ImageTk.PhotoImage(img)
        self.lab1=tk.Label(self,image=self.my_img)
        self.lab1.place(x=0,y=10)

        #text
        self.lab2=tk.Label(self,text="Search by doc names or file names or browse it.Run clone will open\nit for you")
        self.lab2.place(x=35,y=15)

        #dropdown
        # in drop down we get a feature to take entry as well
        self.lab3=tk.Label(self,text="Open:")
        self.lab3.place(x=0,y=70)
        self.present_items=StringVar()
        self.menu=[]
        if os.path.exists("Items.csv"):
            self.file=open("Items.csv")
            reader=csv.reader(self.file,delimiter=" ")
            for i in reader:
                self.menu.insert(0,i[0])
        self.entry=ttk.Combobox(self,textvariable=self.present_items,values=self.menu,width=50)
        self.entry.pack(side="bottom",padx=(40,20),pady=(0,70))
        self.entry.focus_set()#enabling cursor 

        #buttons
        self.btn1=tk.Button(self,text="Ok",width=5,font=(6),padx=5,pady=3,relief="ridge",command=self.open)
        self.btn1.place(x=100,y=110)

        self.btn2=tk.Button(self,text="Browse",width=5,font=(6),padx=5,pady=3,relief="ridge",command=self.browse)
        self.btn2.place(x=180,y=110)

        self.btn2=tk.Button(self,text="Cancel",width=5,font=(6),padx=5,pady=3,relief="ridge",command=self.destroy)
        self.btn2.place(x=260,y=110)


    def item(self,a):
        """to get items in self.menu"""
        # self.menu.append(a)
        #we need to insert the file dir at the 0 the index for using it as a file history
        self.menu.insert(0,a)
        self.entry["values"]=self.menu
        self.present_items.set(self.menu[0])
        #opening a file to get the datas
        csvfile=open("Items.csv","a",newline="")
        writer=csv.writer(csvfile,delimiter=' ')
        writer.writerow([self.menu[0]])
        csvfile.close()

        # csv allow us to write in row by default
        return
    def open(self):
        try:
            file=self.present_items.get()
            os.startfile(f"{file}")
            return self.item(file)
        except Exception as e:
            print(e) 
            return showerror(title="Run clone",message="File not found.Plz check the spelling.")
    def browse(self):
        # filetype=(('text files', '*.txt'),('All files', '*.*'))
        self.dir="D:"   
        filetype=[("Python Files",".py"),("All files","*.*")]
        try:
            #filename=fd.askopenfilename(title="Open file",filetypes=filetype)#it will allow us to select single file
            filedir=fd.askopenfilenames(title="Open file",filetypes=filetype,initialdir=self.dir)#it will allow us to select multiple files
            for i in filedir:
                os.startfile(i)
                return self.item(i)
        except Exception as e:
            print(e)
            return showerror(title="Run clone",message="File not found.Plz check the spelling.")

app=Win() 
app.mainloop()
