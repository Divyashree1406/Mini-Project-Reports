from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tempfile, os
import empdatabase

#frontend

class Employee:

     def __init__(self,root) :
          self.root = root
          self.root.title("empbook")
          self.root.geometry("1350x800+0+0")
          self.root.configure(bg='gainsboro')

          MainFrame =  Frame(self.root, bd=10, width=1350, height=700, relief=RIDGE)
          MainFrame.grid()

          TopFrame1  = Frame(MainFrame, bd=7, width=1340, height=50, relief=RIDGE)
          TopFrame1.grid(row=2, column = 0)

          TopFrame2  =  Frame(MainFrame, bd=7, width=1340, height=100, relief=RIDGE)
          TopFrame2.grid(row=1, column = 0)

          TopFrame3  =  Frame(MainFrame, bd=7, width=1340, height=500, relief=RIDGE)
          TopFrame3.grid(row=0, column = 0)

          LeftFrame = Frame(TopFrame3 , bd=5, width=1340, height=400, padx=2, bg="gainsboro", relief=RIDGE)
          LeftFrame.pack(side=LEFT)
          LeftFrame1 = Frame(LeftFrame , bd=5, width=600,  height=180, padx=4, pady=4, bg="gainsboro", relief=RIDGE )
          LeftFrame1.pack(side=TOP)

          LeftFrame2 = Frame(LeftFrame ,  bd=5,  width=600,  height=180, padx=2, bg="gainsboro" , relief=RIDGE)
          LeftFrame2.pack(side=TOP)
          LeftFrame2Left = Frame(LeftFrame2 ,  bd=5,  width=300,  height=170, padx=2, bg="gainsboro" , relief=RIDGE)
          LeftFrame2Left.pack(side=LEFT)
          LeftFrame2Right = Frame(LeftFrame2 ,  bd=5,  width=300,  height=170, padx=2, bg="gainsboro" , relief=RIDGE)
          LeftFrame2Right.pack(side=RIGHT)

          RightFrame1 = Frame(TopFrame3 , bd=5, width=320, height=400, padx=2, bg="gainsboro", relief=RIDGE)
          RightFrame1.pack(side=RIGHT)
          RightFrame1a = Frame(RightFrame1 , bd=5, width=310, height=300, padx=2, bg="gainsboro", relief=RIDGE)
          RightFrame1a.pack(side=TOP)

          RightFrame2 = Frame(TopFrame3 , bd=5, width=300, height=400, padx=2, bg="gainsboro", relief=RIDGE)
          RightFrame2.pack(side=RIGHT)
          RightFrame2a = Frame(RightFrame2 , bd=5, width=280, height=50, padx=2, bg="gainsboro", relief=RIDGE)
          RightFrame2a.pack(side=TOP)
          RightFrame2b = Frame(RightFrame2 , bd=5, width=280, height=180, padx=2, bg="gainsboro", relief=RIDGE)
          RightFrame2b.pack(side=TOP)
          RightFrame2c = Frame(RightFrame2 , bd=5, width=280, height=100, padx=2, bg="gainsboro", relief=RIDGE)
          RightFrame2c.pack(side=TOP)
          RightFrame2d = Frame(RightFrame2 , bd=5, width=280, height=50, padx=2, bg="gainsboro", relief=RIDGE)
          RightFrame2d.pack(side=TOP)

          #=============================Functions===============================================
          def addData():
               if(len(Reference.get())!=0):
                    empdatabase.addEmployeeRec(Reference.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(),Mobile.get(), NINumber.get(),
                    stdLoan.get(), Tax.get(), Pension.get(), Deductions.get(), NetPay.get(), GrossPay.get())
                    lstEmployee.delete(0,END)
                    lstEmployee.insert(END,(Reference.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(),Mobile.get(), NINumber.get(),
                    stdLoan.get(), Tax.get(), Pension.get(), Deductions.get(), NetPay.get(), GrossPay.get()))

          def DisplayData():
               lstEmployee.delete(0,END)
               for row in empdatabase.viewData():
                    lstEmployee.insert(END, row, str(""))

          def EmployeeRec(event):
               global Ed
               searchEd = lstEmployee.curselection()[0]
               Ed = lstEmployee.get(searchEd)

               self.txtReference.delete(0,END)
               self.txtReference.insert(END,Ed[1])
               self.txtFirstname.delete(0,END)
               self.txtFirstname.insert(END,Ed[2])
               self.txtSurname.delete(0,END)
               self.txtSurname.insert(END,Ed[3])
               self.txtAddress.delete(0,END)
               self.txtAddress.insert(END,Ed[4])
               self.txtGender.delete(0,END)
               self.txtGender.insert(END,Ed[5])
               self.txtMobile.delete(0,END)
               self.txtMobile.insert(END,Ed[6])
               self.txtNINumber.delete(0,END)
               self.txtNINumber.insert(END,Ed[7])
               self.txtstdLoan.delete(0,END)
               self.txtstdLoan.insert(END,Ed[8])
               self.txtTax.delete(0,END)
               self.txtTax.insert(END,Ed[9])
               self.txtPension.delete(0,END)
               self.txtPension.insert(END,Ed[10])
               self.txtDeductions.delete(0,END)
               self.txtDeductions.insert(END,Ed[11])
               self.txtNetPay.delete(0,END)
               self.txtNetPay.insert(END,Ed[12])
               self.txtGrossPay.delete(0,END)
               self.txtGrossPay.insert(END,Ed[13])

          def DeleteData():
               if(len(Reference.get())!=0):
                    empdatabase.deleteRec(Ed[0])
                    Reset()
                    DisplayData()

          def searchData():
               lstEmployee.delete(0,END)
               for row in empdatabase.searchData(Reference.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(),Mobile.get(), NINumber.get(),
                    stdLoan.get(), Tax.get(), Pension.get(), Deductions.get(), NetPay.get(), GrossPay.get()):
                    lstEmployee.insert(END, row, str(""))

          def update():
               if(len(Reference.get())!=0):
                    empdatabase.deleteRec(Ed[0])
               if(len(Reference.get())!=0):
                  empdatabase.addEmployeeRec(Reference.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(),Mobile.get(), NINumber.get(),
                    stdLoan.get(), Tax.get(), Pension.get(), Deductions.get(), NetPay.get(), GrossPay.get())
                  lstEmployee.delete(0,END)
                  lstEmployee.insert(END,(Reference.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(),Mobile.get(), NINumber.get(),
                    stdLoan.get(), Tax.get(), Pension.get(), Deductions.get(), NetPay.get(), GrossPay.get()))
                  
               

          def iPrint():
               q = self.txtReceipt.get("1.0", "end-1c")
               filename = tempfile.mktemp(".doc")
               open (filename, "w"). write(q)
               os.startfile(filename, "Print")

          def  Reset():
               global Ed
               Firstname.set(" ")
               Surname.set(" ")
               Address.set(" ")
               Reference.set(" ")
               Surname.set(" ")
               CityWeighting.set(" ")
               Mobile.set(" ")
               BasicSalary.set(" ")
               OverTime.set(" ")
               GrossPay.set(" ")
               NetPay.set(" ")
               Tax.set(" ")
               Pension.set(" ")
               stdLoan.set(" ")
               NIPayment.set(" ")
               Deductions.set(" ")
               Gender.set(" ")
               Payday.set(" ")
               TaxPeriod.set(" ")
               NINumber.set(" ")
               NICode.set(" ")
               TaxablePay.set(" ")
               PensionablePay.set(" ")
               TaxCode.set(" ")
               OtherPaymentDue.set("0.00")
               self.txtReceipt.delete("1.0",END)

          def iQuit():
               iQuit = tkinter.messagebox.askyesno("empbook","Do you really want to exit?")
               if iQuit > 0:
                    root.destroy()
                    return

          def PayRef():
               Payday.set(time.strftime("%d/%m/%Y"))
               Refpay = random.randint(16462, 7084009)
               Refpaid = ("Ref" +str(Refpay))
               Reference.set(Refpaid)

               NIpay = random.randint(40005, 408400)
               NIpaid = ("NI" +str(NIpay))
               NINumber.set(NIpay)

               iDate = datetime.datetime.now()
               TaxPeriod.set(iDate.month)

               NCode = random.randint(1556, 13976)
               CodeNI = ("NIC" + str(NCode))
               NICode.set(CodeNI)

               iTaxCode = random.randint(7556, 15976)
               PaymentTaxCode = ("TCode" + str(iTaxCode))
               TaxCode.set(PaymentTaxCode)

                          
          def MonthlySalary():
               PayRef()

               BS= float(BasicSalary.get())
               CW= float(CityWeighting.get())
               OT= float(OverTime.get())
               OPD= float(OtherPaymentDue.get())

               MTax = ( (BS+CW+OT+OPD) *0.3)
               TTax = "Rs",str('%.2f'%(MTax))
               Tax.set(TTax)

               M_Pension = ((BS + CW + OT + OPD) * 0.02)
               MM_Pension = "Rs",str('%.2f'%(M_Pension))
               Pension.set(MM_Pension)

               M_stdLoan = ((BS +CW+OT+OPD)* 0.012)
               MM_stdLoan = "Rs",str('%.2f'%(M_stdLoan))
               stdLoan.set(MM_stdLoan)
                                     
               M_NIPayment = ((BS +CW+OT+OPD)* 0.011)
               MM_NIPayment  = "Rs",str('%.2f'%(M_NIPayment))
               NIPayment.set(MM_NIPayment)

               Deduct = (MTax + M_Pension + M_stdLoan + M_NIPayment)
               Deduct_Payment = "Rs",str('%.2f'%(Deduct))
               Deductions.set(Deduct_Payment)
               Gross_Pay = "Rs",str('%.2f'%( BS + CW + OT + OPD))
               GrossPay.set(Gross_Pay)

               NetPayAfter = (BS +CW+OT+OPD) - Deduct
               NetAfter = "Rs",str('%.2f'%(NetPayAfter))
               NetPay.set(NetAfter)

               TaxablePay.set(TTax)
               PensionablePay.set(MM_Pension)

               self.txtReceipt.insert(END,'\t\t Monthly Pay Slip' +"\n\n")
               self.txtReceipt.insert(END,'Reference: \t\t'+Reference.get() +"\n")
               self.txtReceipt.insert(END,'Reference: \t\t'+Payday.get() +"\n")
               self.txtReceipt.insert(END,'Employer Name:\t\t'+ Firstname.get() +"\n")
               self.txtReceipt.insert(END,'Employer Name:\t\t'+ Surname.get() +"\n\n")
               self.txtReceipt.insert(END,'Tax:\t\t'+ Tax.get() +"\n")
               self.txtReceipt.insert(END,'Pension:\t\t'+ Pension.get() +"\n")
               self.txtReceipt.insert(END,'Student Loan:\t\t'+ stdLoan.get() +"\n")
               self.txtReceipt.insert(END,'NI Number:\t\t'+ NINumber.get() +"\n")
               self.txtReceipt.insert(END,'NI Payment:\t\t'+ NIPayment.get() +"\n")
               self.txtReceipt.insert(END,'Deductions:\t\t'+ Deductions.get() +"\n")
               self.txtReceipt.insert(END,'City Weighting:\t\t'+ str('Rs %.2f' %(CityWeighting.get())) +"\n")

               self.txtReceipt.insert(END,'\nTax Paid:\t\t'+ str('Rs %.2f' %(BasicSalary.get())) +"\n")
               self.txtReceipt.insert(END,'OverTime:\t\t'+ "Rs" +OverTime.get() +"\n")
               self.txtReceipt.insert(END,'NetPay:\t\t'+ "Rs" +NetPay.get() +"\n")
               self.txtReceipt.insert(END,'GrossPay:\t\t'+ GrossPay.get() +"\n")

               addData()
               

               

               
               
          #=============================variables===============================================
          global Ed
          Firstname = StringVar()
          Surname = StringVar()
          Address = StringVar()
          Reference = StringVar()
          Surname = StringVar()
          CityWeighting = IntVar()
          Mobile = StringVar()
          BasicSalary = IntVar()
          OverTime = StringVar()
          GrossPay = StringVar()
          NetPay = StringVar()
          Tax = StringVar()
          Pension = StringVar()
          stdLoan = StringVar()
          NIPayment = StringVar()
          Deductions = StringVar()
          Gender = StringVar()
          Payday = StringVar()
          TaxPeriod = StringVar()
          NINumber = StringVar()
          NICode = StringVar()
          TaxablePay = StringVar()
          PensionablePay = StringVar()
          OtherPaymentDue = StringVar()
          TaxCode = StringVar()

          CityWeighting.set(" ")
          BasicSalary.set(" ")
          OtherPaymentDue.set("0.00")
          #==================================Receipt=====================================================================
          self.txtReceipt = Text(RightFrame1a, height=23, width=42, bd=10, font=('arial',9,'bold'))
          self.txtReceipt.grid(row=0, column = 0)
          #============================================================================================================
          self.lblLabel = Label (TopFrame2, font=('arial', 10 , 'bold'), padx=6,pady=2, text="Reference\tFirstname\tSurname\tAddress\t\tGender\tMobile\tNI Number\tStudent Loan\tTax\tPension\t Deductions\tNet Pay\tGross Pay")
          self.lblLabel.grid(row = 0, column=0, columnspan=17)
          #================================Listbox and scrollbar==========Receipt==============================================
          scrollbar = Scrollbar(TopFrame2)
          scrollbar.grid(row = 0, column=1, sticky=' ns ')

          lstEmployee = Listbox(TopFrame2, width = 145, height=5, font=('arial' , 12 , 'bold'), yscrollcommand=scrollbar.set)
          lstEmployee.bind('<<ListboxSelect>>',EmployeeRec)
          lstEmployee.grid(row=1, column=0, padx=1, sticky='nsew')
          scrollbar.config(command = lstEmployee.xview)
          #===================================Widget===================================================================
          self.lblReference = Label(LeftFrame1, font=('arial' , 12 , 'bold'), text="Reference", bd=7, bg='gainsboro',  anchor='w')
          self.lblReference.grid(row=0, column = 0)
          self.txtReference =Entry(LeftFrame1, font=('arial' , 12 , 'bold'), bd=5, width= 60, justify = 'left' , textvariable=Reference )
          self.txtReference.grid(row=0, column = 1)

          self.lblFirstname = Label(LeftFrame1, font=('arial' , 12 , 'bold'), text="Firstname", bd=7,  bg='gainsboro', anchor='w')
          self.lblFirstname.grid(row=1, column = 0)
          self.txtFirstname =Entry(LeftFrame1, font=('arial' , 12 , 'bold'), bd=5, width= 60, justify = 'left' , textvariable=Firstname )
          self.txtFirstname.grid(row=1, column = 1)

          self.lblSurname = Label(LeftFrame1, font=('arial' , 12 , 'bold'), text="Surname", bd=7, bg='gainsboro',  justify=LEFT)
          self.lblSurname.grid(row=2, column = 0)
          self.txtSurname =Entry(LeftFrame1, font=('arial' , 12 , 'bold'), bd=5, width= 60, justify = 'left' , textvariable=Surname )
          self.txtSurname.grid(row=2, column = 1)

          self.lblAddress = Label(LeftFrame1, font=('arial' , 12 , 'bold'), text="Address ", bd=7, bg='gainsboro',  anchor='w')
          self.lblAddress.grid(row=3, column = 0)
          self.txtAddress  =Entry(LeftFrame1, font=('arial' , 12 , 'bold'), bd=5, width= 60, justify = 'left' , textvariable=Address  )
          self.txtAddress .grid(row=3, column = 1)

          self.lblGender = Label(LeftFrame1, font=('arial' , 12 , 'bold'), text="Gender ", bd=7, bg='gainsboro', anchor='w')
          self.lblGender.grid(row=4, column = 0)
          self.txtGender  =Entry(LeftFrame1, font=('arial' , 12 , 'bold'), bd=5, width= 60, justify = 'left' , textvariable=Gender )
          self.txtGender.grid(row=4, column = 1)

          self.lblMobile = Label(LeftFrame1, font=('arial' , 12 , 'bold'), text="Mobile ", bd=7, bg='gainsboro' )
          self.lblMobile.grid(row=5, column = 0)
          self.txtMobile  =Entry(LeftFrame1, font=('arial' , 12 , 'bold'), bd=5, width= 60, justify = 'left' , textvariable=Mobile )
          self.txtMobile.grid(row=5, column = 1)

          
        #============================================================================================================
          self.lblCityWeighting = Label(LeftFrame2Left , font=('arial' , 12 , 'bold'), text="CityWeighting ", bd=7, bg='gainsboro', anchor='e' )
          self.lblCityWeighting.grid(row=0, column = 0, sticky=W)
          self.txtCityWeighting = Entry(LeftFrame2Left , font=('arial' , 12 , 'bold'), textvariable=CityWeighting , bd=5,width=20,justify='left' )
          self.txtCityWeighting.grid(row=0, column = 1)

          self.lblBasicSalary= Label(LeftFrame2Left , font=('arial' , 12 , 'bold'), text="BasicSalary ", bd=7, bg='gainsboro', anchor='w' )
          self.lblBasicSalary.grid(row=1, column = 0, sticky=W)
          self.txtBasicSalary = Entry(LeftFrame2Left , font=('arial' , 12 , 'bold'), textvariable=BasicSalary , bd=5,width=20,justify='left'  )
          self.txtBasicSalary.grid(row=1, column = 1)

          self.lblOverTime= Label(LeftFrame2Left , font=('arial' , 12 , 'bold'), text="OverTime ", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblOverTime.grid(row=2, column = 0, sticky=W)
          self.txtOverTime = Entry(LeftFrame2Left , font=('arial' , 12 , 'bold'), textvariable=OverTime , bd=5,width=20,justify='left'  )
          self.txtOverTime.grid(row=2, column = 1)

          self.lblOtherPaymentDue= Label(LeftFrame2Left , font=('arial' , 12 , 'bold'), text="OtherPaymentDue", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblOtherPaymentDue.grid(row=3, column = 0, sticky=W)
          self.txtOtherPaymentDue = Entry(LeftFrame2Left , font=('arial' , 12 , 'bold'), textvariable=OtherPaymentDue , bd=5,width=20,justify='left'  )
          self.txtOtherPaymentDue.grid(row=3, column = 1)

        #============================================================================================================
          self.lblTax= Label(LeftFrame2Right , font=('arial' , 12 , 'bold'), text="Tax", bd=7, bg='gainsboro', anchor='e' )
          self.lblTax.grid(row=0, column = 0, sticky=W)
          self.txtTax = Entry(LeftFrame2Right , font=('arial' , 12 , 'bold'), textvariable=Tax , bd=5,width=20,justify='left'  )
          self.txtTax.grid(row=0, column = 1)

          self.lblPension= Label(LeftFrame2Right , font=('arial' , 12 , 'bold'), text="Pension", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblPension.grid(row=1, column = 0, sticky=W)
          self.txtPension = Entry(LeftFrame2Right , font=('arial' , 12 , 'bold'), textvariable=Pension , bd=5,width=20,justify='left'  )
          self.txtPension.grid(row=1, column = 1)

          self.lblstdLoan= Label(LeftFrame2Right , font=('arial' , 12 , 'bold'), text="Student Loan", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblstdLoan.grid(row=2, column = 0, sticky=W)
          self.txtstdLoan = Entry(LeftFrame2Right , font=('arial' , 12 , 'bold'), textvariable=stdLoan , bd=5,width=20,justify='left'  )
          self.txtstdLoan.grid(row=2, column = 1)

          self.lblNIPayment= Label(LeftFrame2Right , font=('arial' , 12 , 'bold'), text="NI Payment", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblNIPayment.grid(row=3, column = 0, sticky=W)
          self.txtNIPayment = Entry(LeftFrame2Right , font=('arial' , 12 , 'bold'), textvariable=NIPayment , bd=5,width=20,justify='left'  )
          self.txtNIPayment.grid(row=3, column = 1)

       #============================================================================================================
          self.lblPayday= Label(RightFrame2a , font=('arial' , 12 , 'bold'), text="Payday", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblPayday.grid(row=0, column = 0, sticky=W)
          self.txtPayday = Entry(RightFrame2a , font=('arial' , 12 , 'bold'), textvariable=Payday , bd=5,width=20,justify='left'  )
          self.txtPayday.grid(row=0, column = 1)

          self.lblTaxPeriod= Label(RightFrame2b , font=('arial' , 12 , 'bold'), text="Tax Period", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblTaxPeriod.grid(row=0, column = 0, sticky=W)
          self.txtTaxPeriod = Entry(RightFrame2b , font=('arial' , 12 , 'bold'), textvariable=TaxPeriod , bd=5,width=17,justify='left'  )
          self.txtTaxPeriod.grid(row=0, column = 1)

          self.lblTaxCode= Label(RightFrame2b , font=('arial' , 12 , 'bold'), text="Tax Code", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblTaxCode.grid(row=1, column = 0, sticky=W)
          self.txtTaxCode= Entry(RightFrame2b , font=('arial' , 12 , 'bold'), textvariable=TaxCode , bd=5,width=17,justify='left'  )
          self.txtTaxCode.grid(row=1, column = 1)

          self.lblNINumber= Label(RightFrame2b , font=('arial' , 12 , 'bold'), text="NI Number", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblNINumber.grid(row=2, column = 0, sticky=W)
          self.txtNINumber= Entry(RightFrame2b , font=('arial' , 12 , 'bold'), textvariable=NINumber , bd=5,width=17,justify='left'  )
          self.txtNINumber.grid(row=2, column = 1)

          self.lblNICode= Label(RightFrame2b , font=('arial' , 12 , 'bold'), text="NI Code", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblNICode.grid(row=3, column = 0, sticky=W)
          self.txtNICode= Entry(RightFrame2b , font=('arial' , 12 , 'bold'), textvariable=NICode , bd=5,width=17,justify='left'  )
          self.txtNICode.grid(row=3, column = 1)

          self.lblTaxablePay= Label(RightFrame2c , font=('arial' , 12 , 'bold'), text="Taxable Pay", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblTaxablePay.grid(row=0, column = 0, sticky=W)
          self.txtTaxablePay= Entry(RightFrame2c , font=('arial' , 12 , 'bold'), textvariable=TaxablePay , bd=5,width=17,justify='left'  )
          self.txtTaxablePay.grid(row=0, column = 1)

          self.lblPensionablePay= Label(RightFrame2c , font=('arial' , 12 , 'bold'), text="PensionablePay", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblPensionablePay.grid(row=1, column = 0, sticky=W)
          self.txtPensionablePay= Entry(RightFrame2c , font=('arial' , 12 , 'bold'), textvariable=PensionablePay, bd=5,width=17,justify='left'  )
          self.txtPensionablePay.grid(row=1, column = 1)

          self.lblNetPay= Label(RightFrame2d , font=('arial' , 12 , 'bold'), text="Net Pay", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblNetPay.grid(row=0, column = 0, sticky=W)
          self.txtNetPay= Entry(RightFrame2d , font=('arial' , 12 , 'bold'), textvariable=NetPay, bd=5,width=17,justify='left'  )
          self.txtNetPay.grid(row=0, column = 1)

          self.lblGrossPay= Label(RightFrame2d , font=('arial' , 12 , 'bold'), text="Gross Pay", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblGrossPay.grid(row=1, column = 0, sticky=W)
          self.txtGrossPay= Entry(RightFrame2d , font=('arial' , 12 , 'bold'), textvariable=GrossPay, bd=5,width=17,justify='left'  )
          self.txtGrossPay.grid(row=1, column = 1)

          self.lblDeductions= Label(RightFrame2d , font=('arial' , 12 , 'bold'), text="Deductions", bd=7, bg='gainsboro', anchor='w' , justify=LEFT)
          self.lblDeductions.grid(row=2, column = 0, sticky=W)
          self.txtDeductions= Entry(RightFrame2d , font=('arial' , 12 , 'bold'), textvariable=Deductions, bd=5,width=17,justify='left'  )
          self.txtDeductions.grid(row=2, column = 1) 

     #============================================================================================================

          self.btnAddNewTotal=Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                     width=8, text="AddNew/Total", command=MonthlySalary).grid(row=0, column=0 ,  padx=1)

          self.btnPrint=Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                     width=8, text="Print",command=iPrint).grid(row=0, column=1 ,  padx=1)

          self.btnDisplay=Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                     width=8, text="Display", command=DisplayData).grid(row=0, column=2 ,  padx=1)

          self.btnUpdate=Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                     width=8, text="Update", command= update).grid(row=0, column=3 ,  padx=1)

          self.btnDelete=Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                     width=8, text="Delete", command= DeleteData).grid(row=0, column=4 ,  padx=1)

          self.btnSearch=Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                     width=8, text="Search",command= searchData).grid(row=0, column=5 ,  padx=1)

          self.btnReset=Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                     width=8, text="Reset",command=Reset).grid(row=0, column=6 ,  padx=1)

          self.btnExit=Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                     width=8, text="Exit             ", command=iQuit).grid(row=0, column=7 ,  padx=1)




    #=========================================================================================================


if __name__ ==  '__main__':
                             root = Tk()
                             application = Employee(root)
                             root.mainloop()




    
