from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import tempfile, os
import empdatabase
import empbook
def main():
     root = Tk()
     app = emplogin(root)

class emplogin:
     def __init__(self, master):
          self.master = master
          self.master.title("empbook")
          self.master.geometry("1350x750+0+0")
          self.master.config(bg='cadet blue')
          self.frame = Frame(self.master, bg='cadet blue')
          self.frame.pack()
          
          self.Username = StringVar()
          self.Password = StringVar()

          self.lblTitle = Label(self.frame, text = ' ADMIN LOGIN ', font=('arial',60,'bold'), bg='cadet Blue', fg='cornsilk')
          self.lblTitle.grid(row = 0, column=0, columnspan=2, pady=20)
     #============================================================================================
          self.LoginFrame1 = LabelFrame(self.frame, width=1350, height=300,font=('arial',20,'bold'), relief='ridge', bg='cadet blue',bd=40)
          self.LoginFrame1.grid(row=1, column=0)

          self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=200,font=('arial',20,'bold'), relief='ridge', bg='cadet blue',bd=40)
          self.LoginFrame2.grid(row=2, column=0)
     #====================================================================================================
          self.lblUsername = Label(self.LoginFrame1, text = 'Username' , font=('arial',30,'bold'), bd=22, bg='cadet blue', fg='cornsilk')
          self.lblUsername.grid(row=0, column=0)

          self.lblUsername = Entry(self.LoginFrame1, font=('arial',30,'bold'), bd=7, textvariable=self.Username, width=33)
          self.lblUsername.grid(row=0, column=1, padx=88)

          self.lblPassword = Label(self.LoginFrame1, text = 'Password' , font=('arial',30,'bold'), bd=22, bg='cadet blue', fg='cornsilk')
          self.lblPassword.grid(row=1, column=0)

          self.lblPassword = Entry(self.LoginFrame1, font=('arial',30,'bold'), show='*',bd=7, textvariable=self.Password)
          self.lblPassword.grid(row=1, column=1, columnspan=2, pady=30)
     #=============================================================================================     
          self.btnLogin = Button(self.LoginFrame2, text='Login', width=15, font=('arial',30,'bold'), bg='cadet blue', fg='cornsilk', command = self.Login_System)
          self.btnLogin.grid(row=3, column=0, pady=20, padx=8)

          self.btnReset = Button(self.LoginFrame2, text='Reset', width=15, font=('arial',30,'bold'), bg='cadet blue', fg='cornsilk',command = self.iReset)
          self.btnReset.grid(row=3, column=1, pady=20, padx=8)

          self.btniExit= Button(self.LoginFrame2, text='Exit', width=15, font=('arial',30,'bold'), bg='cadet blue', fg='cornsilk',command = self.iExit)
          self.btniExit.grid(row=3, column=2, pady=20, padx=8)

     #============================================================================================
     def Login_System(self):
          user = (self.Username.get())
          pas = (self.Password.get())
          if(user == str(user) and pas == str(123)):
                    os.system('empbook.py')
          else:
                tkinter.messagebox.showerror("empbook","Invalid details")
                self.Username.set("")
                self.Password.set("")

     def iReset(self):
          self.Username.set("")
          self.Password.set("")

     def iExit(self):
          self.iExit = tkinter.messagebox.askyesno("empbook","Confirm if you want to exit")
          if self.iExit > 0:
               self.master.destroy()
               return
          

     





#=================================================================================================         
if __name__ == '__main__':
     main()


#========================================================================================================


