from tkinter import *
from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
import pandas as pd
from PIL import Image, ImageTk
data=pd.read_excel('database_updated.xlsx')
model=list(data['Device Model'])
serial=list(data['Device Serial No'])
print(serial)
assigned=list(data['Assigned to'])
location=list(data['Location'])
name=list(data['Model name'])
invoice=list(data['Invoice number'])
date=list(data['Date Received'])

class Table:
	
	def __init__(self,root,lst,total_rows,total_columns):
        
        
		
		# code for creating table
		for i in range(total_rows):
			for j in range(total_columns):
				
				self.e = Entry(root, width=20, fg='black',
							font=('Arial',10,'bold'))
				
				self.e.grid(row=i, column=j)
				self.e.insert(END, lst[i][j])
                
# GUI
root = Tk()
root.title("Chatbot")
root.state('zoomed')
root.configure(background='blue')
 
BG_GRAY = "blue"
BG_COLOR = "blue"
TEXT_COLOR = "black"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
def search6():
    print("ready")
    d6=e6.get()
    print(invoice)
    lst6 = [('Device Model','Device Serial No','Assigned to','Location','ModelName','Invoice Number','date Received')]
    found=0
    print(d6)
    for i in range(len(invoice)):
        
        if(int(d6)==int(invoice[i])):
            print("found")
            found=1
            
            lst6.append((model[i],serial[i],assigned[i],location[i],name[i],invoice[i],date[i]))
           
            
    if(found==0):
        txt.insert(END, "\n" + "Machine -> Invalid search , Search Agasin or Type close ")
    else:
     
        total_rows = len(lst6)
        total_columns = len(lst6[0])
	
        new_window=Toplevel(root)
        app=Table(new_window,lst6,total_rows,total_columns)
        txt.insert(END, "\n" + "Machine -> Type close ")
        
def search5():
    print("ready")
    d5=e5.get()
    print(assigned)
    lst5 = [('Device Model','Device Serial No','Assigned to','Location','ModelName','Invoice Number','date Received')]
    found=0
    print(d5)
    for i in range(len(name)):
        
        if((d5)==(name[i])):
            print("found")
            found=1
            
            lst5.append((model[i],serial[i],assigned[i],location[i],name[i],invoice[i],date[i]))
           
            
    if(found==0):
        txt.insert(END, "\n" + "Machine -> Invalid search , Search Agasin or Type close ")
    else:
     
        total_rows = len(lst5)
        total_columns = len(lst5[0])
	
        new_window=Toplevel(root)
        app=Table(new_window,lst5,total_rows,total_columns)
        txt.insert(END, "\n" + "Machine -> Type close ")
        
def search4():
    print("ready")
    d4=e4.get()
    print(assigned)
    lst4 = [('Device Model','Device Serial No','Assigned to','Location','ModelName','Invoice Number','date Received')]
    found=0
    print(d4)
    for i in range(len(location)):
        
        if((d4)==(location[i])):
            print("found")
            found=1
            
            lst4.append((model[i],serial[i],assigned[i],location[i],name[i],invoice[i],date[i]))
           
            
    if(found==0):
        txt.insert(END, "\n" + "Machine -> Invalid search , Search Agasin or Type close ")
    else:
     
        total_rows = len(lst4)
        total_columns = len(lst4[0])
	
        new_window=Toplevel(root)
        app=Table(new_window,lst4,total_rows,total_columns)
        txt.insert(END, "\n" + "Machine -> Type close ")
        
def search3():
    print("ready")
    d3=e3.get()
    print(assigned)
    lst3 = [('Device Model','Device Serial No','Assigned to','Location','ModelName','Invoice Number','date Received')]
    found=0
    print(d3)
    for i in range(len(assigned)):
        
        if((d3)==(assigned[i])):
            print("found")
            found=1
            
            lst3.append((model[i],serial[i],assigned[i],location[i],name[i],invoice[i],date[i]))
           
            
    if(found==0):
        txt.insert(END, "\n" + "Machine -> Invalid search , Search Agasin or Type close ")
    else:
     
        total_rows = len(lst3)
        total_columns = len(lst3[0])
	
        new_window=Toplevel(root)
        app=Table(new_window,lst3,total_rows,total_columns)
        txt.insert(END, "\n" + "Machine -> Type close ")
        
def search2():
    print("ready")
    d2=e2.get()
    print(serial)
    lst1 = [('Device Model','Device Serial No','Assigned to','Location','ModelName','Invoice Number','date Received')]
    found=0
    print(d2)
    for i in range(len(serial)):
        
        if(int(d2)==int(serial[i])):
            print("found")
            found=1
            
            lst1.append((model[i],serial[i],assigned[i],location[i],name[i],invoice[i],date[i]))
           
            
    if(found==0):
        txt.insert(END, "\n" + "Machine -> Invalid search , Search Agasin or Type close ")
    else:
     
        total_rows = len(lst1)
        total_columns = len(lst1[0])
	
        new_window=Toplevel(root)
        app=Table(new_window,lst1,total_rows,total_columns)
        txt.insert(END, "\n" + "Machine -> Type close ")
        
def search1():
    print("ready")
    d1=e1.get()
    lst = [('Device Model','Device Serial No','Assigned to','Location','ModelName','Invoice Number','date Received')]
    found=0
    print(d1)
    for i in range(len(model)):
        if(d1.lower()==model[i].lower()):
            print("found")
            found=1
            
            lst.append((model[i],serial[i],assigned[i],location[i],name[i],invoice[i],date[i]))
           
            
    if(found==0):
        txt.insert(END, "\n" + "Machine -> Invalid search , Search Agasin or Type close ")
    else:

       
        total_rows = len(lst)
        total_columns = len(lst[0])
	
        #new_window=Toplevel(w)
        new_window=Toplevel(root)
        app=Table(new_window,lst,total_rows,total_columns)
        txt.insert(END, "\n" + "Machine -> Type close ")
        
# Send function
def send():
    
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
 
    user = e.get().lower()
    
    if (user == "hello"):
        txt.insert(END, "\n" + "Machine -> Hi there, Want to Search Something"+"\n"+" Press Yes/No")
    elif(user=="yes"):
        txt.insert(END, "\n" + "Machine ->"+"\n"+"1. Search By Model No"+"\n"+"2 Search By Serial No"
                   +"\n"+"3 Search By Assignend To"+"\n"+"4 Search By Location"
                   +"\n"+"5 Search By Device Name"
                   +"\n"+"6 Search By Invoice No"
                   +"\n"+"Type your option ")
    elif(user=="no"):
       txt.insert(END, "\n" + "Machine -> Thankyou , BYY") 
       root.destroy()
    elif(user=="1"):
        txt.insert(END, "\n" + "Machine -> Enter Device Model in pop up Frame or type Close:") 
        frame1.place(x=800,y=10, height=400, width=400)
    elif(user=="2"):
         txt.insert(END, "\n" + "Machine -> Enter Device Serial No in pop up Frame or type Close:") 
         frame2.place(x=800,y=10, height=400, width=400)
    elif(user=="3"):
         txt.insert(END, "\n" + "Machine -> Enter Device Assigned to in pop up Frame or type Close:") 
         frame3.place(x=800,y=10, height=400, width=400)
    elif(user=="4"):
         txt.insert(END, "\n" + "Machine -> Enter LOcation to in pop up Frame or type Close:") 
         frame4.place(x=800,y=10, height=400, width=400)
    elif(user=="5"):
          txt.insert(END, "\n" + "Machine -> Enter Device Name to in pop up Frame or type Close:") 
          frame5.place(x=800,y=10, height=400, width=400)
    elif(user=="6"):
              txt.insert(END, "\n" + "Machine -> Enter Device Name to in pop up Frame or type Close:") 
              frame6.place(x=800,y=10, height=400, width=400)
    elif(user=='close'):
        frame1.place_forget()
        frame2.place_forget()
        frame3.place_forget()
        frame4.place_forget()
        frame5.place_forget()
        frame6.place_forget()

        txt.insert(END, "\n" + "Machine -> Want to Search again? Yes/No") 
        

    else:
        txt.insert(END, "\n" + "Machine -> Sorry! I didn't understand that")
 
    e.delete(0, END)
 
 

 
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.insert(END, "\n" + "Machine-> Type Hello to start....")
txt.place(x=20,y=60)
 
scrollbar = Scrollbar(txt)
scrollbar.place()
 
e = Entry(root, bg="blue", fg=TEXT_COLOR, font=FONT, width=55)
e.place(x=20,y=600)
 
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).place(x=650,y=600)

defaultImg = Image.open('img.jpg')
defaultPhoto = ImageTk.PhotoImage(defaultImg)
img_lb=Label(root)
img_lb.configure(image=defaultPhoto)
img_lb.place(x=800, y=60, width=500, height=550)
frame1=Frame(root,bd=10,relief=FLAT,bg='white')
frame1.place(x=800,y=10, height=400, width=400)
frame1.place_forget()
e1 = Entry(frame1, fg='blue', font=FONT, width=55)
e1.place(x=10,y=40)
send = Button(frame1, text="Seach for Device Model", font=FONT_BOLD, bg=BG_GRAY,
              command=search1).place(x=10,y=100)


frame2=Frame(root,bd=10,relief=FLAT,bg='white')
frame2.place(x=800,y=10, height=400, width=400)
frame2.place_forget()
e2 = Entry(frame2, fg='black', font=FONT, width=55)
e2.place(x=10,y=40)
send2 = Button(frame2, text="Seach for Serial Number", font=FONT_BOLD, bg=BG_GRAY,
              command=search2).place(x=10,y=100)


frame3=Frame(root,bd=10,relief=FLAT,bg='white')
frame3.place(x=800,y=10, height=400, width=400)
frame3.place_forget()
e3 = Entry(frame3, fg='black', font=FONT, width=55)
e3.place(x=10,y=40)
send3 = Button(frame3, text="Seach for Assigned To", font=FONT_BOLD, bg=BG_GRAY,
              command=search3).place(x=10,y=100)


frame4=Frame(root,bd=10,relief=FLAT,bg='white')
frame4.place(x=800,y=10, height=400, width=400)
frame4.place_forget()
e4 = Entry(frame4, fg='black', font=FONT, width=55)
e4.place(x=10,y=40)
send4 = Button(frame4, text="Seach for Location", font=FONT_BOLD, bg=BG_GRAY,
              command=search4).place(x=10,y=100)

frame5=Frame(root,bd=10,relief=FLAT,bg='white')
frame5.place(x=800,y=10, height=400, width=400)
frame5.place_forget()
e5 = Entry(frame5, fg='black', font=FONT, width=55)
e5.place(x=10,y=40)
send5 = Button(frame5, text="Seach for Device name", font=FONT_BOLD, bg=BG_GRAY,
              command=search5).place(x=10,y=100)

frame6=Frame(root,bd=10,relief=FLAT,bg='white')
frame6.place(x=800,y=10, height=400, width=400)
frame6.place_forget()
e6 = Entry(frame6, fg='blue', font=FONT, width=55)
e6.place(x=10,y=40)
send6 = Button(frame6, text="Seach for Invoice_number", font=FONT_BOLD, bg=BG_GRAY,
              command=search6).place(x=10,y=100)

root.mainloop()