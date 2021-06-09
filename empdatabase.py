import sqlite3

def EmployeeData():
     con = sqlite3.connect( "Employee.db")
     cur = con.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS Employee (id INTEGER PRIMARY KEY, Reference text, \
     Firstname text, Surname text, Address text , Gender text, Mobile text, NINumber text, stdLoan text, Tax text, \
     Pension text, Deductions text, NetPay text, GrossPay text)")
     con.commit()
     con.close()

def addEmployeeRec(Reference, Firstname, Surname, Address, Gender, Mobile, NINumber, stdLoan, Tax, Pension, Deductions, NetPay, GrossPay):
     con = sqlite3.connect("Employee.db")
     cur = con.cursor()
     cur.execute("INSERT INTO Employee VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?)",\
                 (Reference, Firstname, Surname, Address, Gender, Mobile, NINumber, stdLoan, Tax, Pension, Deductions, NetPay, GrossPay))
     con.commit()
     con.close()

def viewData():
     con = sqlite3.connect("Employee.db")
     cur = con.cursor()     
     cur.execute("SELECT * FROM Employee")
     rows = cur.fetchall()
     con.close()
     return rows

def deleteRec(id):
     con = sqlite3.connect("Employee.db")
     cur = con.cursor()     
     cur.execute("DELETE  FROM Employee WHERE id=?", (id,))
     con.commit()
     con.close()
     
def searchData(Reference= "", Firstname= "", Surname= "", Address= "", Gender= "", Mobile= "", NINumber= "", stdLoan= "", Tax= "", Pension= "", Deductions= "", NetPay= "", GrossPay= ""):
     con = sqlite3.connect("Employee.db")
     cur = con.cursor()
     cur.execute("SELECT * FROM Employee WHERE Reference = ? oR Firstname =? oR Surname = ? oR Address =? oR Gender =? oR Mobile =? oR NINumber =? oR stdLoan =? oR Tax =? oR Pension =? oR Deductions=? oR NetPay =? oR GrossPay=?",\
                  (Reference, Firstname, Surname, Address, Gender, Mobile, NINumber, stdLoan, Tax, Pension, Deductions, NetPay, GrossPay))
     rows = cur.fetchall()
     con.close()
     return rows

def dataUpdate(Reference= "", Firstname= "", Surname= "", Address= "", Gender= "", Mobile= "", NINumber= "", stdLoan= "", Tax= "", Pension= "", Deductions= "", NetPay= "", GrossPay= ""):
     con = sqlite3.connect("Employee.db")
     cur = con.cursor()
     cur.execute("UPDATE Employee SET Reference = ? , Firstname =? , Surname = ? ,dress =? , Gender =? , Mobile =? , NINumber =? , stdLoan =?  , Tax =? , Pension =? , Deductions=? , NetPay =? , GrossPay=?",\
                  (Reference, Firstname, Surname, Address, Gender, Mobile, NINumber, stdLoan, Tax, Pension, Deductions, NetPay, GrossPay , id))
     con.commit()
     con.close()
     


EmployeeData()



