import mysql.connector
import datetime
from tabulate import tabulate




mydb=mysql.connector.connect(host="localhost",user="root",password="mysql",database="no")
mycursor=mydb.cursor()


mycursor=mydb.cursor()

Tablename=input("Name of the table:")
if Tablename=="Rishi":

    while True:
        print('Main Menu')
        print('1. Adding Employee record')
        print('2. For displaying record of all employes')
        print('3. For displaying record of a particular employe')
        print('4. For deleting record of employes')
        print('5. For deleting recors of particular emloye')
        print('6. For modification in a record')
        print('7. For displaying payroll')
        print('8. For exit')
        print('9. Change tables')
        print("Enter choice..",end='')
        choice=int(input())
        if choice==1:
            print("Enter emplyoee information")
            while True:
                mempno=int(input("Enter the employee no:"))
                mname=input("Enter employee name:")
                mjob=input("Enter employee job:")
                mbasic=float(input("Enter basic salary:"))
                query="insert into "+Tablename+"(empno,name,job,Basicsalary) values({0},'{1}','{2}',{3})".format(mempno,mname,mjob,mbasic)
                mycursor.execute(query)
                mydb.commit()
                k=input("Do you want to add more records (y/n):")
                print("Recors added sucessfully")
                if k=='n':
                     break

        elif choice==2:
            query="select * from "+Tablename+";"
            mycursor.execute(query)
            print(tabulate(mycursor,headers=['EmpNo','Name','Job','Basic Salary'],tablefmt='fancy_grid'))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords:
            print(rec)'''

        elif choice==3:
            en=input("Enter employee no. of the record to be displayed:")
            query="select * from "+Tablename+" where empno="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\nRecord of Employee No:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==-1:
                   print("Nothing to display")   
        elif choice==4:
            ch=input("Do you want to delet all the records (y/n)")
            if ch.upper()=="Y":
                mycursor.execute("delete from "+Tablename)
                mydb.commit()
                print("All records are deleted..")
        elif choice==5:
            en=int(input("Enter employee no. of records to be deleted:"))
            query='delete from '+Tablename+' where empno='+str(en)
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print("eletion done")
            else:
                print("Employee no ",en,"not found")
        elif choice==6:
            en=input("Enter employee no. of the record to be modified")
            query='select * from '+Tablename+' where empno='+str(en)
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print('Empno '+en+' does not exist')
            else:
                mname=myrecord[1]
                mjob=myrecord[2]
                mbasic=myrecord[3]
                print('empno :',myrecord[0])
                print('name  :',myrecord[1])
                print('job   :',myrecord[2])
                print('basic :',myrecord[3])
                print('---------------------')
                print('Type value to modify below or just press enter for no change')
                x=input('Enter name:')
                if len(x)>0:
                    mname=x
                x=input('Enter job:')
                if len(x)>0:
                    mjob=x
                x=input('Enter basic salary:')
                if len(x)>0:
                     mbasic=float(x)
                query='update '+Tablename+' set name='+"'"+mname+"'"+',job='+"'"+mjob+"'"+',basicsalary='+str(mbasic)+' where empno='+str(en)
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print('Record modified')
        elif choice==7:
                query='select * from '+Tablename+';'
                mycursor.execute(query)
                myrecords=mycursor.fetchall()
                print("\n\n\n")
                print(95*'*')
                print('Employee payroll'.center(90))
                print(95*'*')
                now=datetime.datetime.now()
                print("current date and time",end=' ')
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
                print()
                print(95*'-')
                print('%-5s %-15s %-10s %-8s'\
                      %('Empno','Name','Job','Basic'))
                print(95*'-')
                    
                print(tabulate(myrecords))
                print(95*'-')
        elif choice==8:
            break
        elif choice==9:
            
            G=input("Do you want to change the table?:")
            if G=='n':
                continue
            if G=='y':
                while True:
                    
                        print('Main Menu')
                        print('1. Adding leave details of different catagories')
                        print('2. For displaying details of all catagories')
                        print('3. For displaying Net salary with names')
                        print('4. changing tables')
                        print("Enter choice..",end='')
                        choice=int(input())
                        if choice==1:
                            print("Enter emplyoee information")
                            while True:
                                    P=int(input("Enter employee no:"))
                                    mem=input("Enter the Catagories:")
                                    mna=int(input("Enter days of leave taken:"))
                                    mbas=float(input("Enter basic salary:"))
                                    if mna>3:
                                        
                                        msam=mbas*0.5
                                        mnet=mbas-msam
                                    print(mnet)
                                    query="insert into fiffi(Empno,Catagory,Days_of_leave,Basicsalary,Net_salary) values({0},'{1}',{2},{3},{4})".format(P,mem,mna,mbas,mnet)
                                    mycursor.execute(query)
                                    mydb.commit()
                                    k=input("Do you want to add more records (y/n):")
                                    print("Recors added sucessfully")
                                    if k=='n':
                                        break
                                          
                            
                        elif choice==2:
                            query="select * from fiffi;"
                            mycursor.execute(query)
                            print(tabulate(mycursor,headers=['Empno','Catagory','Days_of_leave','Basic_Salary','Net_Salary'],tablefmt='fancy_grid'))
                            '''myrecords=mycursor.fetchall()
                            for rec in myrecords:
                            print(rec)'''
                        elif choice==3:
                        
                            query= "select * from rishi natural join fiffi ;"
                            mycursor.execute(query)
                            print(tabulate(mycursor,headers=['Employee_no','Basicsalary','Name','Job','Catagory','Day_leave','Net_salary'],tablefmt='fancy_grid'))
                            '''myrecords=mycursor.fetchall()
                            for rec in myrecords:
                            print(rec)'''
                        elif choice==4:
                            break
                    
                          
                            
                
                


                
                

