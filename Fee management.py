#drop database school;
#create database school;
#use school;
#create table student(roll int(5) primary key, name varchar(20) not null, age int(2) not null, class int(3), city varchar(10));
#create table fee(roll int(5) references student(roll), FeeDeposit int(6) not null, month varchar(10));

import mysql.connector
db=mysql.connector.connect(host="localhost", user="root", passwd="root", database="school")
cursor=db.cursor()
def AddStudent():
    L=[]
    Roll=int(input("Enter roll number:"))
    Name=input("Enter name:")
    Age=int(input("Enter age:"))
    Class=int(input("Enter class:"))
    City=input("Enter city:")
    L.extend([Roll, Name, Age, Class, City])
    student=(L)
    sql="insert into student(Roll, Name, Age, Class, City) values (%s, %s, %s, %s, %s)"
    cursor.execute(sql, student)
    db.commit()
    print("Record has been added")
    RunAgain()
def SearchStudent():
    print("Select the search criteria:")
    print("1. Roll")
    print("2. Name")
    print("3. Age")
    print("4. City")
    print("5. Show all records")
    choice=int(input("Enter corresponding number to select option:"))
    if (choice==1):
        s=int(input("Enter Roll number:"))
        roll=(s,)
        sql="select * from student where roll=%s"
        cursor.execute(sql, roll)
        result=cursor.fetchall()
        for i in result:
            print(i)
        RunAgain()
    elif (choice==2):
        s=input("Enter Name:")
        name=(s,)
        sql="select * from student where name=%s"
        cursor.execute(sql, name)
        result=cursor.fetchall()
        for i in result:
            print(i)
        RunAgain()
    if (choice==3):
        s=int(input("Enter Age:"))
        age=(s,)
        sql="select * from student where age=%s"
        cursor.execute(sql, age)
        result=cursor.fetchall()
        for i in result:
            print(i)
        RunAgain()
    elif (choice==4):
        s=input("Enter City:")
        city=(s,)
        sql="select * from student where city=%s"
        cursor.execute(sql, city)
        result=cursor.fetchall()
        for i in result:
            print(i)
        RunAgain()
    elif (choice==5):
        sql="select * from student"
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in result:
            print(i)
        RunAgain()
    else:
        print("Invalid Choice: Please Enter a number from 1-5")
        RunAgain()
def DepositFee():
    L=[]
    Roll=int(input("Enter roll number:"))
    FeeDeposit=int(input("Enter Fees to be deposited:"))
    Month=input("Enter month:")
    L.extend([Roll, FeeDeposit, Month])
    fee=(L)
    sql="insert into fee(Roll, FeeDeposit, Month) values (%s, %s, %s)"
    cursor.execute(sql, fee)
    db.commit()
    print("Fees deposited")
    RunAgain()
def ViewFee():
    print("Enter details of student -")
    roll=int(input("Enter roll number:"))
    sql=("select student.roll, student.name, student.class, sum(fee.feeDeposit), fee.month from student inner join fee on student.roll=fee.roll and fee.roll=%s")
    t=(roll,)
    cursor.execute(sql, t)
    result=cursor.fetchall()
    for i in result:
        if i[0]==None:
            print("Record does not exist")
        else:
            print(i)
    RunAgain()
def RemoveStudent():
    roll=int(input("Enter roll number of the student to be deleted:"))
    t=(roll,)
    sql="delete from fee where roll=%s"
    cursor.execute(sql, t)
    sql="delete from student where roll=%s"
    cursor.execute(sql, t)
    db.commit()
    print("Record deleted")
    RunAgain()
def ShowMenu():
    print("1. Add Student")
    print("2. Search and view any student's data")
    print("3. Deposit Fee")
    print("4. Remove Student")
    print("5. View Fee of any Student")
    print("6. Exit")
    choice=int(input("Enter corresponding number to select option:"))
    if (choice==1):
        AddStudent()
    elif (choice==2):
        SearchStudent()
    elif (choice==3):
        DepositFee()
    elif (choice==4):
        RemoveStudent()
    elif (choice==5):
        ViewFee()
    elif (choice==6):
        print("Thank you for using our application")
    else:
        print("Invalid Choice: Please Enter a number from 1-5")
        RunAgain()
def RunAgain():
    choice=input("Do you want to run again? (y/n):")
    if (choice=="y"):
        ShowMenu()
    elif (choice=="n"):
        print("Thank you for using our application")
    else:
        print("Invalid choice: Please enter 'y' or 'n'")
        RunAgain()
ShowMenu()
