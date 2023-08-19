from tkinter import *
import time
from tkinter import PhotoImage
import ttkthemes
from tkinter import ttk,messagebox
import pymysql
#funcionality

def connect_database():
    def connect():
        try:
            con=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password=PasswordEntry.get())
            mycursor=con.cursor()
            messagebox.showinfo('Sucess','Database Connection is Successfull',parent=connect_window)
        except:
            messagebox.showerror('error','Invalid Details',parent=connect_window)
        query='create patient management system' 
        mycursor.execute(query)  
            
            
    connect_window=Toplevel()
    connect_window.grab_set()
    connect_window.geometry('470x250+730+230')
    connect_window.title('Database connection')
    connect_window.resizable(0,0)
    
    
    
    hostnamelable=Label(connect_window,text="Host name",font=('arial',20,'bold'))
    hostnamelable.grid(row=0,column=0,padx=20)
    
    hostEntry=Entry(connect_window,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)
    
    
    usernamelable=Label(connect_window,text="User-name",font=('arial',20,'bold'))
    usernamelable.grid(row=1,column=0,padx=20)
    
    usernameEntry=Entry(connect_window,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)
    
    
    
    Passwordlable=Label(connect_window,text="Password",font=('arial',20,'bold'))
    Passwordlable.grid(row=2,column=0,padx=20)
    
    PasswordEntry=Entry(connect_window,font=('roman',15,'bold'),bd=2)
    PasswordEntry.grid(row=2,column=1,padx=40,pady=20)
    
    
    conButton=ttk.Button(connect_window,text='Connect',command=connect)
    conButton.grid(row=3,columnspan=2)
    










count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count] #s
    sliderLabel.config(text=text)
    count +=1
    sliderLabel.after(300,slider)






def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLable.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLable.after(1000,clock)
    















#gui
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('equilux')
root.geometry('1174x680+0+0')

root.resizable(False,False)
root.title('Clinic management system')









# Add other widgets and elements on top of the background image label







## Creating date time
datetimeLable = Label(root,text='hello',font=('times new roman',18,'bold'))
datetimeLable.place(x=5,y=5)


clock()



####SLIDER TEXT TOP OF THE PAGE 

s='Clinic management system'
sliderLabel=Label(root,text=s,font=('times new roman',28,'italic bold'))
sliderLabel.place(x=400,y=0)
slider()


#database button

connectButton=ttk.Button(root,text="Connect to database",command=connect_database)
connectButton.place(x=1000,y=0)


###left frame

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)


logo_image=PhotoImage(file="C:\\Users\\TEJAS KENI\\Desktop\\BE project\\Clinic system with  medical insurance predictor\\cms\\doctor.png")
logo_label=Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)


###BUTTONS

add_patientbutton= ttk.Button(leftFrame,text="add patient",width=25,state=DISABLED)
add_patientbutton.grid(row=1, column=0,pady=20)


search_patientbutton= ttk.Button(leftFrame,text="search patient data",width=25,state=DISABLED)
search_patientbutton.grid(row=2, column=0,pady=20)

delete_patientbutton= ttk.Button(leftFrame,text="delete patient data",width=25,state=DISABLED)
delete_patientbutton.grid(row=3, column=0,pady=20)


update_patientbutton= ttk.Button(leftFrame,text="update patient data",width=25,state=DISABLED)
update_patientbutton.grid(row=4, column=0,pady=20)


show_patientbutton= ttk.Button(leftFrame,text="show patient data",width=25,state=DISABLED)
show_patientbutton.grid(row=5, column=0,pady=20)


export_patientbutton= ttk.Button(leftFrame,text="export patient data",width=25,state=DISABLED)
export_patientbutton.grid(row=6, column=0,pady=20)

exit_button= ttk.Button(leftFrame,text="Exit",width=25)
exit_button.grid(row=7, column=0,pady=20)



#### RIGHT FRAME

rightFrame =Frame(root,bg="yellow")
rightFrame.place(x=350,y=80,width=820,height=600)


##scroll bar for frame
ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame,orient=VERTICAL)

ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)
















Patient_Table=ttk.Treeview(rightFrame,columns=('ID','Name','Mobile no.','Email','Gender','DOB','Added date','Disease','Medicines','Appointment','Fee'),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
Patient_Table.pack(fill=BOTH,expand=1)

ScrollbarX.config(command=Patient_Table.xview)
ScrollbarY.config(command=Patient_Table.yview)


Patient_Table.heading('ID',text='ID')
Patient_Table.heading('Name',text='Name')
Patient_Table.heading('Mobile no.',text='Mobile No')
Patient_Table.heading('Email',text='Email address')
Patient_Table.heading('Gender',text='Gender')
Patient_Table.heading('DOB',text='DOB')
Patient_Table.heading('Added date',text='First visit')
Patient_Table.heading('Disease',text='Disease')
Patient_Table.heading('Medicines',text='Medicines given')
Patient_Table.heading('Appointment',text='Next Appointment')
Patient_Table.heading('Fee',text='Total fee')
























Patient_Table.config(show='headings')


















root.mainloop()