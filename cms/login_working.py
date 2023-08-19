from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk
###suhhh
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('ERROR','Fields cannot be empty')
    elif usernameEntry.get()=='Tejas' and passwordEntry.get()=='1234':
        messagebox.showinfo('Sucess','Welcome')
        window.destroy()    ## destroys the cuurent window after right details have been entered
        import afterLogin        #####opens the next window
        
        
    else:
        messagebox.showerror('Error','Pls enter correct Doctor credentails ')




window = Tk()
window.title("Login for clinic database management system")








#####IMaGE HERE

backgroundImage=ImageTk.PhotoImage(file='C:\\Users\\TEJAS KENI\\Desktop\\BE project\\Clinic system with  medical insurance predictor\\cms\\background.jpg')


bgLabel=Label(window, image=backgroundImage)
bgLabel.pack()

 





##### LOGO HERE
LoginFrame = Frame(window)
LoginFrame.place(x=730, y=350)

logoImage = PhotoImage(file='C:\\Users\\TEJAS KENI\\Desktop\\BE project\\Clinic system with  medical insurance predictor\\cms\\medical-team.png')


logoLabel=Label(LoginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=20)





###USERNAME PASSWORD
usernameImage=PhotoImage(file= 'C:\\Users\\TEJAS KENI\\Desktop\\BE project\\Clinic system with  medical insurance predictor\\cms\\user.png')
usernameLabel = Label(LoginFrame, image=usernameImage,text = "Username:  ",compound=LEFT,font=('times new roman',20,'bold'))
usernameLabel.grid(row=1,column=0,pady=10)

###ENTER USERNAME
usernameEntry=Entry(LoginFrame,font=('times new roman',20,'bold'),bd=5)
usernameEntry.grid(row=1,column=1,pady=10)

###ENTER PASSWORD

passwordImage = PhotoImage(file="C:\\Users\\TEJAS KENI\\Desktop\\BE project\\Clinic system with  medical insurance predictor\\cms\\pass.png")
passwordLabel= Label(LoginFrame,image=passwordImage,text='Password:  ', compound=LEFT,font=('times new roman',20,'bold'))
passwordLabel.grid(row=2,column=0,pady=20)
###password entry
passwordEntry=Entry(LoginFrame,font=('times new roman',20,'bold'),bd=5)
passwordEntry.grid(row=2,column=1,pady=20)

####button

loginButton = Button(LoginFrame,text='Login',font=('times new roman',20,'bold'),width=15,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white', cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)







window.mainloop()